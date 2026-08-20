"""Syntara API - A distributed multi-agent system.

A workflow automation platform that combines AI agents, action steps, and human oversight in a visual workflow designer, enabling you to orchestrate complex, multi-step processes across systems.
"""

# ===========================================================
# Import exception classes to trigger exception registration
# -----------------------------------------------------------
from syntara.agent_orchestrator.exceptions import LLMConfigurationError
from syntara.approvals.exceptions import (
    ApprovalAlreadyDecidedError,
    ApprovalAlreadyRequestedError,
    ApprovalNotFoundError,
)
from syntara.core.exceptions import SafeValueError
from syntara.files.exceptions import FileContentNotFoundError, FileError, FileIntegrityError, FileValidationError
from syntara.tool_manager.exceptions import (
    ProviderNameConflictError,
    ProviderNotFoundError,
    ToolBulkUpdateValidationError,
    ToolManagerError,
    ToolNotFoundError,
    ToolRefreshError,
)
from syntara.workflows.exceptions import (
    ExecutionNotFoundError,
    TemporalUnavailableError,
    WorkflowNameConflictError,
    WorkflowNotFoundError,
    WorkflowNotPublishedError,
    WorkflowValidationError,
    WorkflowVersionNotFoundError,
)
