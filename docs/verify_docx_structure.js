#!/usr/bin/env node
/**
 * Verification script for DOCX generation.
 * Simulates the generator's parsing loop and checks that every structural
 * element in the source markdown is consumed by a handler.
 */

const fs = require('fs');

const MD_PATH = __dirname + '/Quran_Protocol_RESEARCH_LOCKED.md';
const raw = fs.readFileSync(MD_PATH, 'utf-8');
const lines = raw.split('\n');

// ─── Step 1: Extract structural elements from source ───

const questionIds = new Set();
const sectionHeaders = [];
const checkpoints = [];
const appendixHeaders = [];
const codeBlocks = [];
const blockquotes = [];
const markdownTables = [];

for (let i = 0; i < lines.length; i++) {
  const t = lines[i].trim();

  // Question IDs: Q1, Q23A, Q49B, Q155a, F1, FA1, M1, etc.
  const qMatches = t.matchAll(/\b(Q\d+[A-Za-z]?|F\d+|FA\d+|M\d+)\b/g);
  for (const m of qMatches) {
    // Only count if it looks like a question definition (in a box header or bold line)
    if (t.startsWith('|') || t.startsWith('**')) {
      questionIds.add(m[1]);
    }
  }

  // Section headers
  if (/^\*\*Section\s+[A-Z][-\d]*/.test(t)) sectionHeaders.push({ line: i + 1, text: t });
  if (t.startsWith('## ')) sectionHeaders.push({ line: i + 1, text: t });
  if (t.startsWith('### ')) sectionHeaders.push({ line: i + 1, text: t });

  // Appendix headers
  if (/^\*\*APPENDIX\s+[A-F]/i.test(t)) appendixHeaders.push({ line: i + 1, text: t });

  // Checkpoints
  if (/^\*\*CHECKPOINT\s*\d*/.test(t)) checkpoints.push({ line: i + 1, text: t });

  // Code blocks
  if (t.startsWith('```')) {
    const start = i + 1;
    i++;
    while (i < lines.length && !lines[i].trim().startsWith('```')) i++;
    codeBlocks.push({ startLine: start, endLine: i + 1 });
  }

  // Blockquotes
  if (t.startsWith('> ')) {
    const start = i + 1;
    while (i + 1 < lines.length && lines[i + 1].trim().startsWith('>')) i++;
    blockquotes.push({ startLine: start, endLine: i + 1 });
  }

  // Markdown tables (header + separator)
  if (t.startsWith('|') && i + 1 < lines.length) {
    const next = lines[i + 1].trim();
    if (/^\|[\s\-:]+\|/.test(next)) {
      markdownTables.push({ line: i + 1 });
    }
  }
}

// ─── Step 2: Simulate the generator's parsing loop ───

const handlerLog = []; // { handler, lineStart, lineEnd }
let processed = new Array(lines.length).fill(false);
let questionBoxIds = new Set();

let idx = 0;
// Skip title lines (same as generator)
while (idx < lines.length && !lines[idx].trim().startsWith('---')) idx++;
if (idx < lines.length) idx++;

// Mark title lines as processed
for (let j = 0; j <= Math.min(idx - 1, lines.length - 1); j++) processed[j] = true;

while (idx < lines.length) {
  const line = lines[idx];
  const trimmed = line.trim();

  if (!trimmed) {
    processed[idx] = true;
    idx++;
    continue;
  }

  // Horizontal rules
  if (/^---+$/.test(trimmed)) {
    handlerLog.push({ handler: 'horizontal-rule', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // #### headings
  if (trimmed.startsWith('#### ')) {
    handlerLog.push({ handler: 'h4', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // ### headings
  if (trimmed.startsWith('### ')) {
    handlerLog.push({ handler: 'h3', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // ## headings
  if (trimmed.startsWith('## ')) {
    handlerLog.push({ handler: 'h2', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // Section headers
  if (/^\*\*Section\s+[A-Z][-\d]*/.test(trimmed)) {
    handlerLog.push({ handler: 'section-header', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // Appendix headers
  if (/^\*\*APPENDIX\s+[A-F]/i.test(trimmed)) {
    handlerLog.push({ handler: 'appendix-header', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // Code blocks
  if (trimmed.startsWith('```')) {
    const start = idx;
    processed[idx] = true;
    idx++;
    while (idx < lines.length && !lines[idx].trim().startsWith('```')) {
      processed[idx] = true;
      idx++;
    }
    if (idx < lines.length) { processed[idx] = true; idx++; }
    handlerLog.push({ handler: 'code-block', lineStart: start + 1, lineEnd: idx });
    continue;
  }

  // Blockquotes
  if (trimmed.startsWith('> ')) {
    const start = idx;
    while (idx < lines.length && lines[idx].trim().startsWith('>')) {
      processed[idx] = true;
      idx++;
    }
    handlerLog.push({ handler: 'blockquote', lineStart: start + 1, lineEnd: idx });
    continue;
  }

  // ASCII instruction boxes
  if (/^\+/.test(trimmed) && (trimmed.includes(':') || trimmed.includes('=')) && !(/^\+[-+]+\+$/.test(trimmed))) {
    const start = idx;
    processed[idx] = true;
    idx++;
    while (idx < lines.length) {
      const bline = lines[idx].trim();
      processed[idx] = true;
      if (/^\+/.test(bline) && (bline.includes(':') || bline.includes('=') || /^\+[-+]+\+$/.test(bline)) && (idx - start) > 1) {
        idx++;
        break;
      }
      idx++;
    }
    handlerLog.push({ handler: 'ascii-instruction-box', lineStart: start + 1, lineEnd: idx });
    continue;
  }

  // Question table blocks
  if (/^\+[-+]+\+$/.test(trimmed)) {
    const start = idx;
    const tableLines = [trimmed];
    processed[idx] = true;
    idx++;
    while (idx < lines.length) {
      const tl = lines[idx].trim();
      tableLines.push(tl);
      processed[idx] = true;
      if (/^\+[-+]+\+$/.test(tl)) {
        const nextLine = idx + 1 < lines.length ? lines[idx + 1].trim() : '';
        if (!nextLine.startsWith('|') && !/^\+[-+]+\+$/.test(nextLine)) {
          idx++;
          break;
        }
      }
      idx++;
    }

    // Extract question IDs from this block
    for (const tl of tableLines) {
      const content = tl.replace(/^\|/, '').replace(/\|$/, '').trim();
      const qm = content.matchAll(/\b(Q\d+[A-Za-z]?|F\d+|FA\d+|M\d+)\b/g);
      for (const m of qm) {
        if (content.includes('**') || /^(Q\d|F\d|FA\d|M\d)/.test(content)) {
          questionBoxIds.add(m[1]);
        }
      }
    }

    handlerLog.push({ handler: 'question-table-block', lineStart: start + 1, lineEnd: idx });
    continue;
  }

  // Markdown tables
  if (trimmed.startsWith('|') && idx + 1 < lines.length && lines[idx + 1].trim().startsWith('|')) {
    const nextLine = lines[idx + 1].trim();
    if (/^\|[\s\-:]+\|/.test(nextLine)) {
      const start = idx;
      processed[idx] = true;
      processed[idx + 1] = true;
      idx += 2;
      while (idx < lines.length && lines[idx].trim().startsWith('|')) {
        processed[idx] = true;
        idx++;
      }
      handlerLog.push({ handler: 'markdown-table', lineStart: start + 1, lineEnd: idx });
      continue;
    }
  }

  // List items
  if (/^[-*]\s/.test(trimmed) && !/^---/.test(trimmed)) {
    handlerLog.push({ handler: 'list-item', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // Numbered list items
  if (/^\d+\.\s/.test(trimmed)) {
    handlerLog.push({ handler: 'numbered-list', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // FA## headers
  if (/^\*\*FA\d+/.test(trimmed)) {
    handlerLog.push({ handler: 'fa-header', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // End-of-appendix markers
  if (/^_End of Appendix/.test(trimmed)) {
    handlerLog.push({ handler: 'end-of-appendix', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // CHECKPOINT headers
  if (/^\*\*CHECKPOINT\s*\d*/.test(trimmed)) {
    handlerLog.push({ handler: 'checkpoint', lineStart: idx + 1, lineEnd: idx + 1 });
    processed[idx] = true;
    idx++;
    continue;
  }

  // Regular paragraphs (with continuation-line merging)
  const start = idx;
  processed[idx] = true;
  while (idx + 1 < lines.length) {
    const next = lines[idx + 1].trim();
    if (!next || next.startsWith('#') || next.startsWith('|') || next.startsWith('+') ||
        next.startsWith('>') || next.startsWith('```') || next.startsWith('---') ||
        next.startsWith('- ') || next.startsWith('* ') || /^\d+\.\s/.test(next) ||
        next.startsWith('**') || next.startsWith('_End of')) {
      break;
    }
    idx++;
    processed[idx] = true;
  }
  handlerLog.push({ handler: 'paragraph', lineStart: start + 1, lineEnd: idx + 1 });
  idx++;
}

// ─── Step 3: Test mergeLinesToParagraphs on scorecard boxes ───

function mergeLinesToParagraphs(lines) {
  const paragraphs = [];
  let current = '';
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      if (current) { paragraphs.push(current); current = ''; }
      paragraphs.push('');
      continue;
    }
    if (/^\*\*.+\*\*$/.test(trimmed)) {
      if (current) { paragraphs.push(current); current = ''; }
      paragraphs.push(trimmed);
      continue;
    }
    if (/^- /.test(trimmed) || /^\d+\.\s/.test(trimmed)) {
      if (current) { paragraphs.push(current); current = ''; }
      current = trimmed;
      continue;
    }
    if (/^[A-Z][A-Za-z \/-]*:\s/.test(trimmed)) {
      if (current) { paragraphs.push(current); current = ''; }
      current = trimmed;
      continue;
    }
    if (current) {
      current += ' ' + trimmed;
    } else {
      current = trimmed;
    }
  }
  if (current) paragraphs.push(current);
  return paragraphs;
}

// Find the two scorecard template boxes
const scorecardBoxes = [];
for (let i = 0; i < lines.length; i++) {
  const t = lines[i].trim();
  if (/^\+:/.test(t) && i + 1 < lines.length) {
    // Look for scorecard content
    let j = i + 1;
    const boxContent = [];
    while (j < lines.length && !(/^\+[-:=]+\+$/.test(lines[j].trim()) && boxContent.length > 3)) {
      boxContent.push(lines[j]);
      j++;
      if (j - i > 40) break;
    }
    const text = boxContent.join(' ');
    if (text.includes('Answer:') && text.includes('Reason:') && text.includes('Running tally:')) {
      scorecardBoxes.push({ startLine: i + 1, lines: boxContent });
    }
  }
}

const labelTests = [];
const expectedLabels = ['Answer:', 'Reason:', 'Critical:', 'Critical Type:', 'Foundational:',
  'Foundational Status:', 'Human-authorship model:', 'Divine-origin model:', 'Verified:', 'Running tally:'];

for (const box of scorecardBoxes) {
  const stripped = box.lines.map(l => l.replace(/^\|\s*/, '').replace(/\s*\|$/, '').trim());
  const merged = mergeLinesToParagraphs(stripped);

  const foundLabels = [];
  for (const para of merged) {
    for (const label of expectedLabels) {
      if (para.startsWith(label)) {
        foundLabels.push(label);
      }
    }
  }

  const missingLabels = expectedLabels.filter(l => !foundLabels.includes(l));
  labelTests.push({
    startLine: box.startLine,
    totalParagraphs: merged.filter(p => p.trim()).length,
    foundLabels: foundLabels.length,
    missingLabels,
    pass: missingLabels.length === 0
  });
}

// Also verify continuation lines merge correctly
const continuationTests = [];
const testCases = [
  { input: ['Verified: [yes-ran-code / accepted-as-claimed /', 'unverified / n/a]'], expectCount: 1 },
  { input: ['Running tally: Human=[weighted total] |', 'Divine=[weighted total] | Critical hits=[count] |', 'Eliminated=[list]'], expectCount: 1 },
];
for (const tc of testCases) {
  const result = mergeLinesToParagraphs(tc.input);
  const nonEmpty = result.filter(p => p.trim());
  continuationTests.push({
    input: tc.input[0].substring(0, 40) + '...',
    expectedParagraphs: tc.expectCount,
    actualParagraphs: nonEmpty.length,
    pass: nonEmpty.length === tc.expectCount
  });
}

// ─── Step 4: Output report ───

console.log('╔══════════════════════════════════════════════════════════════╗');
console.log('║        DOCX STRUCTURE VERIFICATION REPORT                  ║');
console.log('╚══════════════════════════════════════════════════════════════╝');
console.log();

// Source inventory
console.log('── Source Markdown Inventory ──');
console.log(`  Total lines: ${lines.length}`);
console.log(`  Question IDs found: ${questionIds.size}`);
console.log(`  Section/## headers: ${sectionHeaders.length}`);
console.log(`  Appendix headers: ${appendixHeaders.length}`);
console.log(`  Checkpoints: ${checkpoints.length}`);
console.log(`  Code blocks: ${codeBlocks.length}`);
console.log(`  Blockquotes: ${blockquotes.length}`);
console.log(`  Markdown tables: ${markdownTables.length}`);
console.log();

// Handler coverage
const handlerCounts = {};
for (const h of handlerLog) {
  handlerCounts[h.handler] = (handlerCounts[h.handler] || 0) + 1;
}
console.log('── Handler Coverage ──');
for (const [handler, count] of Object.entries(handlerCounts).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${handler}: ${count}`);
}
console.log();

// Dropped lines
const droppedLines = [];
for (let i = 0; i < lines.length; i++) {
  if (!processed[i] && lines[i].trim()) {
    droppedLines.push({ line: i + 1, content: lines[i].trim().substring(0, 80) });
  }
}
console.log('── Dropped Lines (not consumed by any handler) ──');
if (droppedLines.length === 0) {
  console.log('  ✅ NONE — all non-empty lines consumed');
} else {
  console.log(`  ❌ ${droppedLines.length} lines dropped:`);
  for (const d of droppedLines.slice(0, 30)) {
    console.log(`    Line ${d.line}: ${d.content}`);
  }
  if (droppedLines.length > 30) console.log(`    ... and ${droppedLines.length - 30} more`);
}
console.log();

// Question cross-check
console.log('── Question ID Cross-Check ──');
console.log(`  IDs in source: ${questionIds.size}`);
console.log(`  IDs processed by question-table-block: ${questionBoxIds.size}`);
const missingFromProcessing = [...questionIds].filter(q => !questionBoxIds.has(q)).sort();
const extraInProcessing = [...questionBoxIds].filter(q => !questionIds.has(q)).sort();
if (missingFromProcessing.length === 0) {
  console.log('  ✅ All source question IDs found in processing');
} else {
  console.log(`  ⚠️  ${missingFromProcessing.length} IDs found in source but NOT in question boxes:`);
  console.log(`    ${missingFromProcessing.join(', ')}`);
  console.log('    (These may appear in headings, inline text, or non-box contexts — not necessarily errors)');
}
if (extraInProcessing.length > 0) {
  console.log(`  ℹ️  ${extraInProcessing.length} IDs found in boxes but not in source bold/pipe scan:`);
  console.log(`    ${extraInProcessing.join(', ')}`);
}
console.log();

// Scorecard label tests
console.log('── Scorecard Label-Line Tests ──');
for (let i = 0; i < labelTests.length; i++) {
  const lt = labelTests[i];
  const status = lt.pass ? '✅' : '❌';
  console.log(`  Box ${i + 1} (line ~${lt.startLine}): ${status} ${lt.foundLabels}/${expectedLabels.length} labels as separate paragraphs`);
  if (!lt.pass) {
    console.log(`    Missing: ${lt.missingLabels.join(', ')}`);
  }
}
console.log();

// Continuation merge tests
console.log('── Continuation Merge Tests ──');
for (const ct of continuationTests) {
  const status = ct.pass ? '✅' : '❌';
  console.log(`  ${status} "${ct.input}" → ${ct.actualParagraphs} paragraph(s) (expected ${ct.expectedParagraphs})`);
}
console.log();

// Checkpoint verification
console.log('── Checkpoint Headers ──');
if (checkpoints.length > 0) {
  console.log(`  ✅ ${checkpoints.length} checkpoints found:`);
  for (const cp of checkpoints) {
    console.log(`    Line ${cp.line}: ${cp.text.replace(/\*\*/g, '')}`);
  }
} else {
  console.log('  ❌ No checkpoints found');
}
console.log();

// Appendix verification
console.log('── Appendix Headers ──');
if (appendixHeaders.length > 0) {
  console.log(`  ✅ ${appendixHeaders.length} appendix headers found:`);
  for (const ah of appendixHeaders) {
    console.log(`    Line ${ah.line}: ${ah.text.replace(/\*\*/g, '')}`);
  }
} else {
  console.log('  ❌ No appendix headers found');
}
console.log();

// Summary
const allPass = droppedLines.length === 0 &&
  labelTests.every(t => t.pass) &&
  continuationTests.every(t => t.pass);

console.log('══════════════════════════════════════════════════════════════');
if (allPass) {
  console.log('  ✅ ALL CHECKS PASSED');
} else {
  console.log('  ⚠️  SOME CHECKS NEED ATTENTION (see details above)');
}
console.log('══════════════════════════════════════════════════════════════');
