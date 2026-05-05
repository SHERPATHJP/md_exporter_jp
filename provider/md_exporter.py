from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.md_to_pdf.md_to_pdf import MarkdownToPdfTool


class MdExporterProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            tools = [
                MarkdownToPdfTool,
            ]
            for tool in tools:
                tool.from_credentials({})
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
