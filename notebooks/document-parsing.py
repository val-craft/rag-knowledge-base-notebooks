import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
    ## Advanced Document Parsing

    Extracts clean structure from messy PDFs

    [DOCLING](https://www.docling.ai/)
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
