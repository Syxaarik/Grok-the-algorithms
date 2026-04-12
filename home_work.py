import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Задание 4.1 Рекурсивная функция sum()
    """)
    return


@app.cell
def _():
    def sumi(arr):
        if arr == []: # базовый случай, если в массиве 0 элементов
            return 0
        return arr[0] + sumi(arr[1:]) # рекурссия 
    
    print(sumi(arr=[1, 2, 3, 4, 5]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Задание 4.2 рекурсивная функция для подсчета элементов в списке
    """)
    return


@app.cell
def _():
    def rec_counter(arr):
        if arr == []: # базовый случай, если в массиве 0 элементов
            return 0
        return 1 + rec_counter(arr[1:]) # рекурссия 

    print(rec_counter(arr=[1, 2, 3, 4, 5]))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
