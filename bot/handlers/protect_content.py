from fastapi import Request

async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    # Essential security headers for file sharing
    response.headers.update({
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Content-Security-Policy": "default-src 'self'"
    })
    return response
