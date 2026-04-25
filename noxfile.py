import os

import nox


@nox.session(reuse_venv=True, name="test-pydantic-v1")
def test_pydantic_v1(session: nox.Session) -> None:
    # Export uv.lock to a pip-compatible requirements file and install from it.
    # `Session.run_install` would be cleaner but requires nox >= 2024.4.15;
    # we're pinned to 2023.4.22 to match the previous lockfile (see FIXES.md).
    requirements = os.path.join(session.create_tmp(), "requirements-dev.txt")
    session.run(
        "uv", "export", "--group", "dev", "--all-extras", "--frozen",
        "--no-emit-project", "--output-file", requirements,
        external=True,
    )
    session.install("-r", requirements)
    session.install("-e", ".")
    session.install("pydantic<2")

    session.run("pytest", "--showlocals", "--ignore=tests/functional", *session.posargs)
