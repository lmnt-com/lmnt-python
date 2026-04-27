import nox


@nox.session(reuse_venv=True, name="test-pydantic-v1")
def test_pydantic_v1(session: nox.Session) -> None:
    session.run_install(
        "uv", "sync", "--frozen", "--group", "dev", "--all-extras",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True,
    )
    session.install("pydantic<2")
    session.run("pytest", "--showlocals", "--ignore=tests/functional", *session.posargs)
