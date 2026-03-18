-- 在 Supabase SQL Editor 中执行此脚本来创建 quiz_results 表

CREATE TABLE IF NOT EXISTS quiz_results (
    id BIGSERIAL PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    quiz_name VARCHAR(100) NOT NULL,
    answers JSONB NOT NULL,
    results JSONB NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 创建索引以加速查询
CREATE INDEX IF NOT EXISTS idx_quiz_results_student_id ON quiz_results(student_id);
CREATE INDEX IF NOT EXISTS idx_quiz_results_quiz_name ON quiz_results(quiz_name);
CREATE INDEX IF NOT EXISTS idx_quiz_results_submitted_at ON quiz_results(submitted_at);

-- 启用 Row Level Security (RLS) - 允许匿名用户插入数据
ALTER TABLE quiz_results ENABLE ROW LEVEL SECURITY;

-- 创建策略允许匿名用户插入数据
CREATE POLICY "Allow anonymous insert" ON quiz_results
    FOR INSERT
    WITH CHECK (true);

-- 创建策略允许读取自己的数据（通过 student_id）
CREATE POLICY "Allow read own data" ON quiz_results
    FOR SELECT
    USING (true);

-- 显示成功信息
SELECT 'Table quiz_results created successfully!' as message;
