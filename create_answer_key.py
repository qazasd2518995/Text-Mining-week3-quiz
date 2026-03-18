#!/usr/bin/env python3
"""
生成 Week 3 Quiz 答案解析版 PDF - 支持中文
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 注册中文字体
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

# 颜色定义
PAPER = HexColor('#f7f3eb')
INK = HexColor('#2c2416')
INK_LIGHT = HexColor('#5c5142')
ACCENT = HexColor('#c45d3e')
HIGHLIGHT = HexColor('#f4d79e')
SUCCESS = HexColor('#4a7c59')
CODE_BG = HexColor('#e8f5e9')
LIGHT_BG = HexColor('#fdfbf7')

def create_answer_key():
    doc = SimpleDocTemplate(
        "/Users/justin/Text Mining week3 quiz/Week3_Quiz_Answer_Key.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()

    # 自定义样式 - 使用中文字体
    styles.add(ParagraphStyle(
        name='MainTitle',
        fontSize=22,
        leading=28,
        alignment=TA_CENTER,
        textColor=INK,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='Subtitle',
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        textColor=INK_LIGHT,
        spaceAfter=20,
        fontName='Helvetica-Oblique'
    ))

    styles.add(ParagraphStyle(
        name='AnswerKeyBadge',
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=white,
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontSize=13,
        leading=18,
        textColor=white,
        fontName='Helvetica-Bold',
        spaceBefore=20,
        spaceAfter=12,
        leftIndent=10,
        rightIndent=10
    ))

    styles.add(ParagraphStyle(
        name='QuestionText',
        fontSize=11,
        leading=16,
        textColor=INK,
        fontName='Helvetica',
        spaceBefore=14,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='AnswerLabel',
        fontSize=10,
        leading=14,
        textColor=SUCCESS,
        fontName='Helvetica-Bold',
        spaceBefore=4,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='AnswerCode',
        fontSize=11,
        leading=16,
        textColor=SUCCESS,
        fontName='Courier-Bold',
        spaceBefore=4,
        spaceAfter=8,
        leftIndent=20,
    ))

    styles.add(ParagraphStyle(
        name='Explanation',
        fontSize=10,
        leading=14,
        textColor=INK_LIGHT,
        fontName='STSong-Light',  # 中文字体
        spaceBefore=10,
        spaceAfter=18,
        leftIndent=20,
    ))

    styles.add(ParagraphStyle(
        name='ExplanationEN',
        fontSize=10,
        leading=14,
        textColor=INK_LIGHT,
        fontName='Helvetica-Oblique',
        spaceBefore=10,
        spaceAfter=18,
        leftIndent=20,
    ))

    story = []

    # ============ 标题 ============
    # Badge 用表格实现背景色
    badge_table = Table([['ANSWER KEY - Instructor Edition']], colWidths=[250])
    badge_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(badge_table)
    story.append(Spacer(1, 15))

    story.append(Paragraph("Text Mining for Applied Linguistics", styles['MainTitle']))
    story.append(Paragraph("Week 3 Mini Quiz — Vectors, Data Frames &amp; Statistics", styles['Subtitle']))
    story.append(Paragraph("Total: 100 points", styles['Subtitle']))
    story.append(Spacer(1, 15))

    # ============ 情境说明 ============
    story.append(HRFlowable(width="100%", thickness=1, color=INK_LIGHT))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "<b>SCENARIO:</b> You collected data from 6 undergraduate students in the English Department. "
        "Each student reported their daily study hours and their most recent TOEFL iBT total score.",
        styles['QuestionText']
    ))

    # 数据表格
    table_data = [
        ['Student', 'Year', 'Major', 'Daily Study (hrs)', 'TOEFL Score'],
        ['S01', '3', 'ENG', '2.5', '85'],
        ['S02', '4', 'ENG', '4.0', '102'],
        ['S03', '2', 'LING', '1.5', '78'],
        ['S04', '3', 'LING', '3.0', '91'],
        ['S05', '4', 'ENG', '5.0', '110'],
        ['S06', '2', 'LING', '2.0', '82'],
    ]

    data_table = Table(table_data, colWidths=[55, 40, 45, 95, 75])
    data_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), INK),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, INK_LIGHT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_BG]),
    ]))
    story.append(Spacer(1, 10))
    story.append(data_table)
    story.append(Spacer(1, 20))

    # 辅助函数：创建答案框
    def make_answer_box(answer_text, explanation_text):
        """创建带背景色的答案和解释框"""
        from reportlab.platypus import Paragraph as P

        # 使用 Paragraph 让文字自动换行
        ans_style = ParagraphStyle(
            'AnsBox',
            fontName='Courier-Bold',
            fontSize=9,
            leading=13,
            textColor=SUCCESS,
        )
        exp_style = ParagraphStyle(
            'ExpBox',
            fontName='Helvetica-Oblique',
            fontSize=9,
            leading=12,
            textColor=INK_LIGHT,
        )

        answer_para = P(answer_text, ans_style)
        explain_para = P(explanation_text, exp_style)

        answer_table = Table([[answer_para]], colWidths=[450])
        answer_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), CODE_BG),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))

        explain_table = Table([[explain_para]], colWidths=[450])
        explain_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), HIGHLIGHT),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))

        return answer_table, explain_table

    # ============ Q1 ============
    q1_header = Table([['Q1 · Create Three Vectors (20 points)']], colWidths=[470])
    q1_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(q1_header)

    # Q1(a)
    story.append(Paragraph(
        "<b>(a)</b> A numeric vector called <font face='Courier' color='#c45d3e'>year</font> "
        "containing the year of all 6 students <font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "year <- c(3, 4, 2, 3, 4, 2)",
        "Extract values from the Year column in order. The c() function creates a vector."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q1(b)
    story.append(Paragraph(
        "<b>(b)</b> A numeric vector called <font face='Courier' color='#c45d3e'>study</font> "
        "containing the daily study hours <font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "study <- c(2.5, 4.0, 1.5, 3.0, 5.0, 2.0)",
        "Note the decimal points! 4.0 and 4 are equivalent in R."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q1(c)
    story.append(Paragraph(
        "<b>(c)</b> A numeric vector called <font face='Courier' color='#c45d3e'>toefl</font> "
        "containing the TOEFL scores <font color='#c45d3e'>[8 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "toefl <- c(85, 102, 78, 91, 110, 82)",
        "All TOEFL scores are integers. Just extract from the table in order."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # ============ Q2 ============
    story.append(Spacer(1, 15))
    q2_header = Table([['Q2 · Compute Descriptive Statistics (30 points)']], colWidths=[470])
    q2_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(q2_header)

    # Q2(a)
    story.append(Paragraph(
        "<b>(a)</b> What is the mean of the <font face='Courier' color='#c45d3e'>toefl</font> vector? "
        "<font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "R Code: mean(toefl)    Answer: 91.33",
        "mean() calculates the arithmetic average. (85+102+78+91+110+82)/6 = 91.33"
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q2(b)
    story.append(Paragraph(
        "<b>(b)</b> What is the standard deviation of the <font face='Courier' color='#c45d3e'>study</font> vector? "
        "<font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "R Code: sd(study)    Answer: 1.26",
        "sd() calculates the sample standard deviation (denominator n-1)."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q2(c)
    story.append(Paragraph(
        "<b>(c)</b> What is the minimum value in the <font face='Courier' color='#c45d3e'>toefl</font> vector? "
        "<font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "R Code: min(toefl)    Answer: 78",
        "min() returns the smallest value. S03's score of 78 is the lowest."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q2(d)
    story.append(Paragraph(
        "<b>(d)</b> How many students study more than 2.5 hours per day? "
        "<font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "R Code: sum(study > 2.5)    Answer: 3",
        "study > 2.5 creates a logical vector. sum() counts TRUE values as 1."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q2(e)
    story.append(Paragraph(
        "<b>(e)</b> What does <font face='Courier' color='#c45d3e'>toefl / 10</font> produce? "
        "<font color='#c45d3e'>[6 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "Output: [1] 8.5  10.2  7.8  9.1  11.0  8.2",
        "It divides each element by 10. R's vectorized operations apply to each element."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ============ Q3 ============
    q3_header = Table([['Q3 · Build a Data Frame (20 points)']], colWidths=[470])
    q3_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(q3_header)

    # Q3(a)
    story.append(Paragraph(
        "<b>(a)</b> Create the data frame with columns: id, year, major, study, toefl "
        "<font color='#c45d3e'>[12 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))

    code_text = '''id <- c("S01", "S02", "S03", "S04", "S05", "S06")
major <- c("ENG", "ENG", "LING", "LING", "ENG", "LING")
students <- data.frame(id, year, major, study, toefl)'''
    ans, exp = make_answer_box(
        code_text,
        "data.frame() combines vectors into a data frame. Each vector becomes a column."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q3(b)
    story.append(Paragraph(
        "<b>(b)</b> Run <font face='Courier' color='#c45d3e'>str(students)</font>: "
        "How many observations and variables? <font color='#c45d3e'>[4 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "Observations: 6    Variables: 5",
        "str() shows 'data.frame': 6 obs. of 5 variables (6 rows, 5 columns)."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q3(c)
    story.append(Paragraph(
        "<b>(c)</b> Run <font face='Courier' color='#c45d3e'>summary(students)</font>: "
        "What is the median TOEFL score? <font color='#c45d3e'>[4 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "Median TOEFL = 88",
        "Sorted: 78, 82, 85, 91, 102, 110. Median = (85+91)/2 = 88."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # ============ Q4 ============
    story.append(Spacer(1, 15))
    q4_header = Table([['Q4 · Concept Check — Short Answer (30 points)']], colWidths=[470])
    q4_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(q4_header)

    # Q4(a)
    story.append(Paragraph(
        "<b>(a)</b> What is the difference between a vector and a data frame? "
        "<font color='#c45d3e'>[10 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Sample Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "A vector is 1D with same data type. A data frame is 2D table with multiple columns of different types.",
        "Grading: (1) Vector is 1D, data frame is 2D; (2) Vector has one type, data frame can have multiple."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q4(b)
    story.append(Paragraph(
        "<b>(b)</b> What does <font face='Courier' color='#c45d3e'>&lt;-</font> do in R? "
        "How do you read <font face='Courier'>x &lt;- 5</font> out loud? "
        "<font color='#c45d3e'>[10 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Sample Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "<- is the assignment operator. 'x <- 5' is read as 'x gets 5' or 'assign 5 to x'.",
        "Grading: (1) Explain it's an assignment operator; (2) Correctly read as 'gets' or 'assign'."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # Q4(c)
    story.append(Paragraph(
        "<b>(c)</b> What is the difference between <font face='Courier' color='#c45d3e'>mean()</font> "
        "and <font face='Courier' color='#c45d3e'>median()</font>? When might they differ significantly? "
        "<font color='#c45d3e'>[10 pts]</font>",
        styles['QuestionText']
    ))
    story.append(Paragraph("Sample Answer:", styles['AnswerLabel']))
    ans, exp = make_answer_box(
        "mean() = arithmetic average. median() = middle value when sorted. They differ with outliers/skewed data.",
        "Grading: (1) Explain mean vs median calculation; (2) Mention outliers/skewed data cause differences."
    )
    story.append(ans)
    story.append(Spacer(1, 4))
    story.append(exp)
    story.append(Spacer(1, 10))

    # ============ 页尾 ============
    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "This answer key is for instructor use only. Total: 100 points.",
        ParagraphStyle(
            name='Footer',
            fontSize=10,
            alignment=TA_CENTER,
            textColor=INK_LIGHT,
            fontName='Helvetica-Oblique'
        )
    ))

    # 生成 PDF
    doc.build(story)
    print("PDF created: Week3_Quiz_Answer_Key.pdf")

if __name__ == "__main__":
    create_answer_key()
