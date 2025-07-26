# SPEC-mcp

> By DJJ & Danniel
> 
[中文版本](README_ZH.md) | English Version

Mimicking `kiro`'s `SPEC` pattern, following the workflow: Requirements -> Design -> Attention -> TODO -> Implementation

## Usage

### Add MCP Server

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

### Generate Specification Documents

For example, input:

> The key is the last sentence: `call generate_spec`
```text
A web application focused on emotion recording and healing experience, helping users improve mental health and self-awareness through daily mood tracking, diary writing, and data analysis.
Users can record daily mood states, write diaries, upload multimedia content, and understand their emotional change trends through visual data analysis.
The goal is to provide users with a warm and safe digital space to promote emotional management and psychological healing.
MVP doesn't need login/registration features

call generate_spec
```

### Get Specification Documents

```text
call get_spec
```

## Local Development

```bash
git clone https://github.com/TokenRollAI/SPEC-mcp.git

cd SPEC-mcp

uv sync
```