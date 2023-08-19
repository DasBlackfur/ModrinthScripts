def pw_side_from_mr_env(mr_env: dict) -> str:
    server = mr_env["server"] == "required" or mr_env["server"] == "optional"
    client = mr_env["client"] == "required" or mr_env["client"] == "optional"
    if client and server:
        return "both"
    if client:
        return "client"
    if server:
        return "server"
