const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, TableOfContents,
  HeadingLevel, BorderStyle, WidthType, ShadingType, VerticalAlign,
  PageNumber, PageBreak
} = require('docx');

const MD_PATH = __dirname + '/Quran_Protocol_RESEARCH_LOCKED.md';
const OUT_PATH = __dirname + '/Quran_Protocol_RESEARCH_LOCKED.docx';

const raw = fs.readFileSync(MD_PATH, 'utf-8');
const lines = raw.split('\n');

// Color Palette
const COLORS = {
  primary: '1B3A5C',
  secondary: '2E86AB',
  accent: '8B4513',
  boxBg: 'F0F4F8',
  boxBorder: '1B3A5C',
  quoteBg: 'FFF8F0',
  quoteBorder: '8B4513',
  checkboxBg: 'F5F5F5',
  codeBg: 'F5F5F0',
  headerBg: 'E8EEF4',
  white: 'FFFFFF',
  black: '000000',
  gray: '666666',
  lightGray: 'CCCCCC',
  criticalRed: 'CC0000',
  foundationalBlue: '0055AA',
};

const DXA_INCH = 1440;
const PAGE_W = 9360;

const border = (color, size = 1) => ({ style: BorderStyle.SINGLE, size, color });
const cellBorders = (color) => ({
  top: border(color), bottom: border(color),
  left: border(color), right: border(color)
});

function mergeLinesToParagraphs(lines) {
  const paragraphs = [];
  let current = '';
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      // Empty line → paragraph break
      if (current) { paragraphs.push(current); current = ''; }
      paragraphs.push('');
      continue;
    }
    if (/^\*\*.+\*\*$/.test(trimmed)) {
      // Fully-bold line → its own paragraph
      if (current) { paragraphs.push(current); current = ''; }
      paragraphs.push(trimmed);
      continue;
    }
    if (/^- /.test(trimmed) || /^\d+\.\s/.test(trimmed)) {
      // List item or numbered item → starts a new paragraph
      if (current) { paragraphs.push(current); current = ''; }
      current = trimmed;
      continue;
    }
    if (/^[A-Z][A-Za-z \/-]*:\s/.test(trimmed)) {
      // Label line (e.g. "Answer:", "Critical Type:", "Running tally:")
      if (current) { paragraphs.push(current); current = ''; }
      current = trimmed;
      continue;
    }
    // Continuation: append to current paragraph
    if (current) {
      current += ' ' + trimmed;
    } else {
      current = trimmed;
    }
  }
  if (current) paragraphs.push(current);
  return paragraphs;
}

function parseInline(text, overrides = {}) {
  const runs = [];
  // B1: Added bold+italic combos: **_..._** and _**...**_ BEFORE plain **...** match
  const regex = /(\*\*\*(.+?)\*\*\*|\*\*_(.+?)_\*\*|_\*\*(.+?)\*\*_|\*\*(.+?)\*\*|\*(.+?)\*|_(.+?)_|`([^`]+)`|\[CRITICAL\]|\[FOUNDATIONAL\]|\[CODE-DEPENDENT\]|\[METHODOLOGY\s*[—–-]+\s*FORCED NEUTRAL\]|\[PROCEDURAL\]|\[TIER SYSTEM\])/g;
  let last = 0;
  let m;
  const font = overrides.font || 'Georgia';
  const size = overrides.size || 22;
  while ((m = regex.exec(text)) !== null) {
    if (m.index > last) {
      const leftover = text.slice(last, m.index).replace(/\*\*/g, '').replace(/(?<!\w)_|_(?!\w)/g, '');
      if (leftover) runs.push(new TextRun({ text: leftover, font, size, ...overrides }));
    }
    if (m[2]) {
      // ***bold+italic***
      runs.push(new TextRun({ text: m[2], bold: true, italics: true, font, size, ...overrides }));
    } else if (m[3]) {
      // **_bold+italic_**
      runs.push(new TextRun({ text: m[3], bold: true, italics: true, font, size, ...overrides }));
    } else if (m[4]) {
      // _**bold+italic**_
      runs.push(new TextRun({ text: m[4], bold: true, italics: true, font, size, ...overrides }));
    } else if (m[5]) {
      // **bold**
      runs.push(new TextRun({ text: m[5], bold: true, font, size, ...overrides }));
    } else if (m[6]) {
      // *italic*
      runs.push(new TextRun({ text: m[6], italics: true, font, size, ...overrides }));
    } else if (m[7]) {
      // _italic_
      runs.push(new TextRun({ text: m[7], italics: true, font, size, ...overrides }));
    } else if (m[8]) {
      runs.push(new TextRun({ text: m[8], font: 'Courier New', size: 20, ...overrides }));
    } else if (m[0] === '[CRITICAL]') {
      runs.push(new TextRun({ text: '[CRITICAL]', bold: true, color: COLORS.criticalRed, font: 'Arial', size: 20 }));
    } else if (m[0] === '[FOUNDATIONAL]') {
      runs.push(new TextRun({ text: '[FOUNDATIONAL]', bold: true, color: COLORS.foundationalBlue, font: 'Arial', size: 20 }));
    } else if (m[0] === '[CODE-DEPENDENT]') {
      runs.push(new TextRun({ text: '[CODE-DEPENDENT]', bold: true, color: '006600', font: 'Arial', size: 20 }));
    } else if (m[0].includes('FORCED NEUTRAL')) {
      runs.push(new TextRun({ text: m[0], bold: true, color: COLORS.gray, font: 'Arial', size: 20 }));
    } else if (m[0] === '[PROCEDURAL]') {
      runs.push(new TextRun({ text: '[PROCEDURAL]', bold: true, color: COLORS.gray, font: 'Arial', size: 20 }));
    } else if (m[0] === '[TIER SYSTEM]') {
      runs.push(new TextRun({ text: '[TIER SYSTEM]', bold: true, color: COLORS.secondary, font: 'Arial', size: 20 }));
    }
    last = m.index + m[0].length;
  }
  if (last < text.length) {
    // B2: Strip remaining unmatched ** and _ markers from leftover text
    const leftover = text.slice(last).replace(/\*\*/g, '').replace(/(?<!\w)_|_(?!\w)/g, '');
    if (leftover) runs.push(new TextRun({ text: leftover, font, size, ...overrides }));
  }
  if (runs.length === 0) {
    runs.push(new TextRun({ text: text || ' ', font, size, ...overrides }));
  }
  return runs;
}

function makeBox(contentLines, opts = {}) {
  const bgColor = opts.bg || COLORS.boxBg;
  const borderColor = opts.border || COLORS.boxBorder;
  const paragraphs = [];
  const stripped = contentLines.map(line => line.replace(/^\|\s*/, '').replace(/\s*\|$/, '').trim());
  const merged = mergeLinesToParagraphs(stripped);
  for (const text of merged) {
    if (!text) {
      paragraphs.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun({ text: ' ', font: 'Georgia', size: 22 })] }));
      continue;
    }
    paragraphs.push(new Paragraph({
      spacing: { before: 40, after: 40 },
      children: parseInline(text)
    }));
  }
  return new Table({
    columnWidths: [PAGE_W],
    rows: [new TableRow({
      children: [new TableCell({
        borders: cellBorders(borderColor),
        shading: { fill: bgColor, type: ShadingType.CLEAR },
        width: { size: PAGE_W, type: WidthType.DXA },
        children: paragraphs.length ? paragraphs : [new Paragraph({ children: [new TextRun(' ')] })]
      })]
    })]
  });
}

function makeBlockquote(contentLines) {
  const paras = [];
  for (const line of contentLines) {
    const trimmed = line.replace(/^>\s*/, '').trim();
    if (!trimmed) continue;
    const isAttribution = /^[—–-]\s*\*\*/.test(trimmed) || trimmed.startsWith('—');
    if (isAttribution) {
      paras.push(new Paragraph({
        spacing: { before: 60, after: 60 },
        alignment: AlignmentType.RIGHT,
        indent: { left: 200, right: 200 },
        children: parseInline(trimmed)
      }));
    } else {
      paras.push(new Paragraph({
        spacing: { before: 60, after: 60 },
        indent: { left: 200, right: 200 },
        children: parseInline(trimmed, { italics: true, color: COLORS.accent })
      }));
    }
  }
  return new Table({
    columnWidths: [PAGE_W],
    rows: [new TableRow({
      children: [new TableCell({
        borders: {
          top: border(COLORS.quoteBorder, 1),
          bottom: border(COLORS.quoteBorder, 1),
          left: border(COLORS.quoteBorder, 6),
          right: border(COLORS.quoteBorder, 1)
        },
        shading: { fill: COLORS.quoteBg, type: ShadingType.CLEAR },
        width: { size: PAGE_W, type: WidthType.DXA },
        children: paras.length ? paras : [new Paragraph({ children: [new TextRun(' ')] })]
      })]
    })]
  });
}

function makeCodeBlock(codeLines) {
  const paragraphs = [];
  for (const line of codeLines) {
    paragraphs.push(new Paragraph({
      spacing: { before: 20, after: 20 },
      children: [new TextRun({ text: line || ' ', font: 'Courier New', size: 18, color: COLORS.black })]
    }));
  }
  return new Table({
    columnWidths: [PAGE_W],
    rows: [new TableRow({
      children: [new TableCell({
        borders: cellBorders(COLORS.lightGray),
        shading: { fill: COLORS.codeBg, type: ShadingType.CLEAR },
        width: { size: PAGE_W, type: WidthType.DXA },
        children: paragraphs.length ? paragraphs : [new Paragraph({ children: [new TextRun(' ')] })]
      })]
    })]
  });
}

function makeCheckboxRow() {
  const options = ['YES', 'MOSTLY\nYES', 'PARTIALLY\nYES', 'PARTIALLY\nNO', 'MOSTLY\nNO', 'NO'];
  const colW = Math.floor(PAGE_W / 6);
  return new Table({
    columnWidths: Array(6).fill(colW),
    rows: [new TableRow({
      children: options.map(opt => new TableCell({
        borders: cellBorders(COLORS.lightGray),
        shading: { fill: COLORS.checkboxBg, type: ShadingType.CLEAR },
        width: { size: colW, type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        children: opt.split('\n').map((line, idx) => new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: idx === 0 ? 60 : 0, after: 0 },
          children: [
            ...(idx === 0 ? [new TextRun({ text: '\u2610 ', font: 'Arial', size: 20, color: COLORS.primary })] : []),
            new TextRun({ text: line, font: 'Arial', size: 20, bold: true, color: COLORS.primary })
          ]
        }))
      }))
    })]
  });
}

function makeReasoningLine() {
  return new Table({
    columnWidths: [PAGE_W],
    rows: [new TableRow({
      children: [new TableCell({
        borders: cellBorders(COLORS.gray),
        shading: { fill: 'F8F8F8', type: ShadingType.CLEAR },
        width: { size: PAGE_W, type: WidthType.DXA },
        children: [new Paragraph({
          spacing: { before: 100, after: 100 },
          children: [new TextRun({ text: 'Your reasoning:', bold: true, italics: true, font: 'Georgia', size: 22 })]
        })]
      })]
    })]
  });
}

function makeMarkdownTable(headerLine, separatorLine, dataLines) {
  const parseRow = (line) => line.split('|').map(c => c.trim()).filter(c => c !== '');
  const headers = parseRow(headerLine);
  const numCols = headers.length;
  const colW = Math.floor(PAGE_W / numCols);
  const rows = [
    new TableRow({
      tableHeader: true,
      children: headers.map(h => new TableCell({
        borders: cellBorders(COLORS.primary),
        shading: { fill: COLORS.headerBg, type: ShadingType.CLEAR },
        width: { size: colW, type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 60, after: 60 },
          children: parseInline(h)
        })]
      }))
    })
  ];
  for (const line of dataLines) {
    const cells = parseRow(line);
    rows.push(new TableRow({
      children: cells.map(c => new TableCell({
        borders: cellBorders(COLORS.lightGray),
        width: { size: colW, type: WidthType.DXA },
        children: [new Paragraph({
          spacing: { before: 60, after: 60 },
          children: parseInline(c)
        })]
      }))
    }));
  }
  return new Table({ columnWidths: Array(numCols).fill(colW), rows });
}

function buildDocument() {
  const children = [];
  let i = 0;

  // Title Page
  children.push(
    new Paragraph({ spacing: { before: 4000 }, children: [new TextRun({ text: ' ', size: 4 })] }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({ text: 'THE QUR\'AN', font: 'Georgia', size: 56, bold: true, color: COLORS.primary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({ text: 'INVESTIGATION PROTOCOL', font: 'Georgia', size: 56, bold: true, color: COLORS.primary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 400, after: 200 },
      children: [new TextRun({ text: '\u2501'.repeat(40), font: 'Georgia', size: 24, color: COLORS.secondary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 150 },
      children: [new TextRun({ text: 'Research Edition  |  No Pre-Loaded Data', font: 'Georgia', size: 28, color: COLORS.gray })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 150 },
      children: [new TextRun({ text: 'A Structured Evaluation Framework for AI Systems and Critical Readers', font: 'Georgia', size: 24, italics: true, color: COLORS.gray })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 150 },
      children: [new TextRun({ text: '241 Questions  |  5-Point Scale + UNKNOWN  |  Evidence Provided', font: 'Georgia', size: 22, color: COLORS.secondary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 100 },
      children: [new TextRun({ text: 'No Data Pre-Loaded  |  Your Research Builds the Picture', font: 'Georgia', size: 22, color: COLORS.secondary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 200 },
      children: [new TextRun({ text: '\u2501'.repeat(40), font: 'Georgia', size: 24, color: COLORS.secondary })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 100 },
      children: [new TextRun({ text: 'Independent Research Edition', font: 'Georgia', size: 22, italics: true, color: COLORS.gray })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: 'All answers must be based on your own investigation', font: 'Georgia', size: 22, italics: true, color: COLORS.gray })]
    }),
    new Paragraph({ children: [new PageBreak()] })
  );

  // Table of Contents (manual — built from headings in markdown)
  children.push(
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { after: 300 },
      children: [new TextRun({ text: 'Table of Contents', font: 'Georgia', size: 32, bold: true, color: COLORS.primary })]
    })
  );
  for (const tocLine of lines) {
    const tl = tocLine.trim();
    let tocText = null;
    let indent = 0;
    let tocSize = 22;
    let tocBold = false;
    if (tl.startsWith('## ')) {
      tocText = tl.replace(/^##\s+/, '').replace(/\\/g, '');
      indent = 0; tocSize = 22; tocBold = true;
    } else if (/^\*\*Section\s+[A-Z][-\d]*/.test(tl)) {
      tocText = tl.replace(/\*\*/g, '').replace(/\\/g, '');
      indent = 360; tocSize = 22; tocBold = true;
    } else if (/^\*\*APPENDIX\s+[A-I]/i.test(tl)) {
      tocText = tl.replace(/\*\*/g, '').replace(/\\/g, '');
      indent = 0; tocSize = 22; tocBold = true;
    } else if (tl.startsWith('### ')) {
      tocText = tl.replace(/^###\s+/, '').replace(/\\/g, '');
      indent = 360; tocSize = 20;
    }
    if (tocText) {
      children.push(new Paragraph({
        spacing: { before: tocBold ? 80 : 40, after: tocBold ? 80 : 40 },
        indent: { left: indent },
        children: [new TextRun({ text: tocText, font: 'Georgia', size: tocSize, bold: tocBold, color: tocBold ? COLORS.primary : COLORS.gray })]
      }));
    }
  }
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Skip title lines
  i = 0;
  while (i < lines.length && !lines[i].trim().startsWith('---')) i++;
  if (i < lines.length) i++;

  // Parse document
  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    if (!trimmed) { i++; continue; }

    // Horizontal rules
    if (/^---+$/.test(trimmed)) {
      children.push(new Paragraph({
        spacing: { before: 200, after: 200 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: COLORS.lightGray, space: 4 } },
        children: [new TextRun({ text: ' ', size: 4 })]
      }));
      i++;
      continue;
    }

    // #### headings
    if (trimmed.startsWith('#### ')) {
      const text = trimmed.replace(/^####\s+/, '').replace(/\\/g, '');
      children.push(new Paragraph({
        spacing: { before: 250, after: 120 },
        children: [new TextRun({ text, font: 'Georgia', size: 24, bold: true, color: COLORS.secondary })]
      }));
      i++;
      continue;
    }

    // ### headings
    if (trimmed.startsWith('### ')) {
      const text = trimmed.replace(/^###\s+/, '').replace(/\\/g, '');
      children.push(new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 300, after: 150 },
        children: [new TextRun({ text, font: 'Georgia', size: 24, bold: true, color: COLORS.secondary })]
      }));
      i++;
      continue;
    }

    // ## headings
    if (trimmed.startsWith('## ')) {
      const text = trimmed.replace(/^##\s+/, '').replace(/\\/g, '');
      const isSection6 = /SECTION\s+VI/i.test(text);
      children.push(new Paragraph({
        heading: isSection6 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2,
        spacing: { before: 400, after: 200 },
        pageBreakBefore: isSection6,
        children: [new TextRun({ text, font: 'Georgia', size: isSection6 ? 32 : 28, bold: true, color: COLORS.primary })]
      }));
      i++;
      continue;
    }

    // Section headers
    if (/^\*\*Section\s+[A-Z][-\d]*/.test(trimmed)) {
      const text = trimmed.replace(/\*\*/g, '').replace(/\\/g, '');
      children.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 500, after: 200 },
        pageBreakBefore: true,
        children: [new TextRun({ text, font: 'Georgia', size: 28, bold: true, color: COLORS.primary })]
      }));
      i++;
      continue;
    }

    // Appendix headers
    if (/^\*\*APPENDIX\s+[A-I]/i.test(trimmed)) {
      const text = trimmed.replace(/\*\*/g, '').replace(/\\/g, '');
      children.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 500, after: 200 },
        pageBreakBefore: true,
        children: [new TextRun({ text, font: 'Georgia', size: 32, bold: true, color: COLORS.primary })]
      }));
      i++;
      continue;
    }

    // Code blocks
    if (trimmed.startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      if (i < lines.length) i++;
      children.push(makeCodeBlock(codeLines));
      children.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: ' ', size: 4 })] }));
      continue;
    }

    // Blockquotes
    if (trimmed.startsWith('> ')) {
      const quoteLines = [];
      while (i < lines.length && lines[i].trim().startsWith('>')) {
        quoteLines.push(lines[i].trim());
        i++;
      }
      children.push(makeBlockquote(quoteLines));
      children.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: ' ', size: 4 })] }));
      continue;
    }

    // ASCII instruction boxes (must contain : or = in border, not just - and +)
    if (/^\+/.test(trimmed) && (trimmed.includes(':') || trimmed.includes('=')) && !(/^\+[-+]+\+$/.test(trimmed))) {
      const boxLines = [];
      i++;
      while (i < lines.length) {
        const bline = lines[i].trim();
        if (/^\+/.test(bline) && (bline.includes(':') || bline.includes('=') || /^\+[-+]+\+$/.test(bline)) && boxLines.length > 0) {
          i++;
          break;
        }
        boxLines.push(bline);
        i++;
      }
      let bg = COLORS.boxBg;
      let borderCol = COLORS.boxBorder;
      const boxText = boxLines.join(' ');
      if (boxText.includes('MANDATORY OUTPUT') || boxText.includes('MANDATORY:')) {
        bg = 'FFF0F0'; borderCol = COLORS.criticalRed;
      } else if (boxText.includes('FOUNDATIONAL CONSTRAINT')) {
        bg = 'F0F0FF'; borderCol = COLORS.foundationalBlue;
      } else if (boxText.includes('CRITICAL:')) {
        bg = 'FFF5F5'; borderCol = COLORS.criticalRed;
      }
      children.push(makeBox(boxLines, { bg, border: borderCol }));
      children.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: ' ', size: 4 })] }));
      continue;
    }

    // Question table blocks (start with +---+---+)
    if (/^\+[-+]+\+$/.test(trimmed)) {
      const tableLines = [trimmed];
      i++;
      let closingBorders = 0;
      while (i < lines.length) {
        const tl = lines[i].trim();
        tableLines.push(tl);
        if (/^\+[-+]+\+$/.test(tl)) {
          closingBorders++;
          // Check if this is the final closing border
          const nextLine = i + 1 < lines.length ? lines[i + 1].trim() : '';
          if (!nextLine.startsWith('|') && !/^\+[-+]+\+$/.test(nextLine)) {
            i++;
            break;
          }
        }
        i++;
      }

      // Split table content into sections separated by +---+ borders
      const sections = [[]];
      let hasCheckboxes = false;
      let hasReasoning = false;

      for (const tl of tableLines) {
        if (/^\+[-+]+\+$/.test(tl)) {
          if (sections[sections.length - 1].length > 0) sections.push([]);
          continue;
        }
        if (/□/.test(tl)) { hasCheckboxes = true; continue; }
        // Skip checkbox continuation rows (e.g. "| | | YES | NO | | |")
        if (/^\|[\s|]*(YES|NO|MOSTLY|PARTIALLY)[\s|]*(YES|NO)?[\s|]*\|$/.test(tl) && !tl.includes('**')) continue;
        if (/Your reasoning/i.test(tl)) { hasReasoning = true; continue; }
        const content = tl.replace(/^\|/, '').replace(/\|$/, '').trim();
        if (content) sections[sections.length - 1].push(content);
      }
      // Remove empty trailing sections
      while (sections.length > 0 && sections[sections.length - 1].length === 0) sections.pop();

      // First section is the question paragraph (render bold), rest is context
      const questionLines = sections.length > 0 ? sections[0] : [];
      const contextLines = sections.slice(1).reduce((acc, s) => acc.concat(s), []);
      const allText = questionLines.concat(contextLines);

      if (allText.length > 0) {
        const firstLine = allText[0];
        let qBg = COLORS.white;
        let qBorder = COLORS.primary;
        if (firstLine.includes('[CRITICAL]')) {
          qBorder = COLORS.criticalRed; qBg = 'FFFAFA';
        }
        if (firstLine.includes('[FOUNDATIONAL]')) {
          qBorder = COLORS.foundationalBlue; qBg = 'F8F8FF';
        }
        if (firstLine.includes('[CRITICAL]') && firstLine.includes('[FOUNDATIONAL]')) {
          qBorder = '7700AA'; qBg = 'FAF0FF';
        }

        // Build box paragraphs: question paragraph is bold, context is normal
        const boxBg = qBg;
        const boxBorderCol = qBorder;
        const boxParas = [];
        // Question paragraph — join into one bold paragraph
        if (questionLines.length > 0) {
          const qText = questionLines.join(' ').replace(/\*\*/g, '').replace(/(?<!\w)_|_(?!\w)/g, '');
          boxParas.push(new Paragraph({
            spacing: { before: 60, after: 60 },
            children: [new TextRun({ text: qText, font: 'Georgia', size: 22, bold: true })]
          }));
        }
        // Context paragraphs — merge continuation lines, then render
        const mergedContext = mergeLinesToParagraphs(contextLines);
        for (const cl of mergedContext) {
          if (!cl.trim()) {
            boxParas.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun({ text: ' ', font: 'Georgia', size: 22 })] }));
          } else {
            boxParas.push(new Paragraph({
              spacing: { before: 40, after: 40 },
              children: parseInline(cl)
            }));
          }
        }

        children.push(new Table({
          columnWidths: [PAGE_W],
          rows: [new TableRow({
            children: [new TableCell({
              borders: cellBorders(boxBorderCol),
              shading: { fill: boxBg, type: ShadingType.CLEAR },
              width: { size: PAGE_W, type: WidthType.DXA },
              children: boxParas.length ? boxParas : [new Paragraph({ children: [new TextRun(' ')] })]
            })]
          })]
        }));
      }

      if (hasCheckboxes) children.push(makeCheckboxRow());
      if (hasReasoning) children.push(makeReasoningLine());
      children.push(new Paragraph({ spacing: { after: 150 }, children: [new TextRun({ text: ' ', size: 4 })] }));
      continue;
    }

    // Markdown tables
    if (trimmed.startsWith('|') && i + 1 < lines.length && lines[i + 1].trim().startsWith('|')) {
      const headerLine = trimmed;
      const nextLine = lines[i + 1].trim();
      if (/^\|[\s\-:]+\|/.test(nextLine)) {
        i += 2;
        const dataLines = [];
        while (i < lines.length && lines[i].trim().startsWith('|')) {
          dataLines.push(lines[i].trim());
          i++;
        }
        children.push(makeMarkdownTable(headerLine, nextLine, dataLines));
        children.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: ' ', size: 4 })] }));
        continue;
      }
    }

    // List items
    if (/^[-*]\s/.test(trimmed) && !/^---/.test(trimmed)) {
      const listText = trimmed.replace(/^[-*]\s+/, '');
      children.push(new Paragraph({
        spacing: { before: 80, after: 80 },
        indent: { left: 720, hanging: 360 },
        children: [
          new TextRun({ text: '\u2022  ', font: 'Arial', size: 22, color: COLORS.primary }),
          ...parseInline(listText)
        ]
      }));
      i++;
      continue;
    }

    // Numbered list items
    if (/^\d+\.\s/.test(trimmed)) {
      const match = trimmed.match(/^(\d+)\.\s+(.*)/);
      if (match) {
        children.push(new Paragraph({
          spacing: { before: 80, after: 80 },
          indent: { left: 720, hanging: 360 },
          children: [
            new TextRun({ text: match[1] + '.  ', font: 'Georgia', size: 22, bold: true, color: COLORS.primary }),
            ...parseInline(match[2])
          ]
        }));
      }
      i++;
      continue;
    }

    // FA## headers
    if (/^\*\*FA\d+/.test(trimmed)) {
      const text = trimmed.replace(/\*\*/g, '');
      const isFA18 = text.startsWith('FA18');
      if (isFA18) {
        // V9: Decorative separator before FA18
        children.push(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 400, after: 200 },
          children: [new TextRun({ text: '\u2501'.repeat(30), font: 'Georgia', size: 24, color: COLORS.accent })]
        }));
      }
      children.push(new Paragraph({
        spacing: { before: isFA18 ? 400 : 300, after: isFA18 ? 200 : 150 },
        pageBreakBefore: isFA18,
        children: [new TextRun({ text, font: 'Georgia', size: isFA18 ? 30 : 26, bold: true, color: isFA18 ? COLORS.accent : COLORS.primary })]
      }));
      i++;
      continue;
    }

    // End-of-appendix markers
    if (/^_End of Appendix/.test(trimmed)) {
      children.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 200 },
        children: [new TextRun({ text: trimmed.replace(/_/g, ''), italics: true, font: 'Georgia', size: 20, color: COLORS.gray })]
      }));
      i++;
      continue;
    }

    // V12: CHECKPOINT headers
    if (/^\*\*CHECKPOINT\s*\d*/.test(trimmed)) {
      const text = trimmed.replace(/\*\*/g, '');
      children.push(new Paragraph({
        spacing: { before: 400, after: 200 },
        children: [new TextRun({ text, font: 'Georgia', size: 28, bold: true, color: COLORS.secondary })]
      }));
      i++;
      continue;
    }

    // Regular paragraphs
    let paraText = trimmed;
    while (i + 1 < lines.length) {
      const next = lines[i + 1].trim();
      if (!next || next.startsWith('#') || next.startsWith('|') || next.startsWith('+') ||
          next.startsWith('>') || next.startsWith('```') || next.startsWith('---') ||
          next.startsWith('- ') || next.startsWith('* ') || /^\d+\.\s/.test(next) ||
          next.startsWith('**') || next.startsWith('_End of')) {
        break;
      }
      i++;
      paraText += ' ' + lines[i].trim();
    }

    paraText = paraText.replace(/\\\|/g, '|').replace(/\\\[/g, '[').replace(/\\\]/g, ']');

    children.push(new Paragraph({
      spacing: { before: 120, after: 120 },
      children: parseInline(paraText)
    }));
    i++;
  }

  return new Document({
    styles: {
      default: { document: { run: { font: 'Georgia', size: 22 } } },
      paragraphStyles: [
        {
          id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 32, bold: true, color: COLORS.primary, font: 'Georgia' },
          paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 }
        },
        {
          id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 28, bold: true, color: COLORS.primary, font: 'Georgia' },
          paragraph: { spacing: { before: 300, after: 150 }, outlineLevel: 1 }
        },
        {
          id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 24, bold: true, color: COLORS.secondary, font: 'Georgia' },
          paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 }
        }
      ]
    },
    sections: [{
      properties: {
        titlePage: true,
        page: {
          margin: { top: DXA_INCH, right: DXA_INCH, bottom: DXA_INCH, left: DXA_INCH },
          pageNumbers: { start: 1 }
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: 'THE QUR\'AN INVESTIGATION PROTOCOL', font: 'Georgia', size: 16, color: COLORS.gray, italics: true }),
              new TextRun({ text: '  |  ', font: 'Georgia', size: 16, color: COLORS.lightGray }),
              new TextRun({ text: 'Research Edition', font: 'Georgia', size: 16, color: COLORS.gray, italics: true })
            ]
          })]
        }),
        first: new Header({
          children: [new Paragraph({ children: [new TextRun({ text: ' ', size: 4 })] })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            border: { top: { style: BorderStyle.SINGLE, size: 1, color: COLORS.lightGray, space: 4 } },
            spacing: { before: 100 },
            children: [
              new TextRun({ text: 'Page ', font: 'Georgia', size: 18, color: COLORS.gray }),
              new TextRun({ children: [PageNumber.CURRENT], font: 'Georgia', size: 18, color: COLORS.gray }),
              new TextRun({ text: ' of ', font: 'Georgia', size: 18, color: COLORS.gray }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], font: 'Georgia', size: 18, color: COLORS.gray })
            ]
          })]
        })
      },
      children
    }]
  });
}

async function main() {
  console.log('Parsing markdown (' + lines.length + ' lines)...');
  const doc = buildDocument();
  console.log('Generating DOCX...');
  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(OUT_PATH, buffer);
  console.log('Written to: ' + OUT_PATH);
  console.log('File size: ' + (buffer.length / 1024 / 1024).toFixed(2) + ' MB');
}

main().catch(function(e) { console.error(e); process.exit(1); });
