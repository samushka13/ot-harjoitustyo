from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_html(ctx):
    ctx.run("coverage html")

@task(coverage)
def coverage_xml(ctx):
    ctx.run("coverage xml")
