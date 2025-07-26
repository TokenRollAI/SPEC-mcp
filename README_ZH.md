# SPEC-mcp

> By DJJ & Danniel
> 
中文版本 | [English Version](README.md)

模仿`kiro`的`SPEC`模式, 按照 需求 -> 设计 -> 注意事项 -> TODO -> 实现

## 使用

### 添加MCP 

```json
{
    "mcpServers": {
        "spec-mcp": {
            "command": "uvx",
            "args": [
                "mcp-spec@latest"
            ]
        }
    }
}

```

### 生成需求文档

例如输入:

> 重点是最后一句: `call generate_spec`
```text
一个专注于情绪记录和疗愈体验的web应用，帮助用户通过日常情绪记录、日记写作和数据分析来提升心理健康和自我认知。
·用户可以每天记录心情状态、撰写日记并上传多媒体内容，通过可视化数据分析了解自己的情绪变化趋势。
·目标是为用户提供一个温暖、安全的数字空间，促进情绪管理和心理疗愈。
MVP不需要登录/注册这些功能

call generate_spec
```

### 获取需求文档

```text
call get_spec
```

## 本地调试

```bash
git clone https://github.com/TokenRollAI/SPEC-mcp.git

cd SPEC-mcp

uv sync
```

