import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('dados_aleatorios.csv')

def total_vendas(dataframe, linha="Produto", colum_vendas='Vendas'):
    total_vendas= dataframe.groupby(linha)[colum_vendas].sum().to_dict()

    return total_vendas


def graphic_yearly_measure(dataframe, product,rotate_index=0,figsize_index=(5,5), month_row='Mes',line="Produto", sell_row='Vendas'):
    sale_by_month = dataframe[dataframe[line] == product].groupby(month_row)[sell_row].sum().reindex(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], fill_value=0)

    plt.figure(figsize=figsize_index)
    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.bar(sale_by_month.index, sale_by_month.values, color='orange')
    plt.title(f'Venda de {product} ao longo do ano')
    plt.xticks(rotation=rotate_index)

    plt.tight_layout()
    plt.show()


def prod_top_month(dataframe, month_row='Mes',line="Produto", sell_row='Vendas'):
    idx = dataframe.groupby(line)[sell_row].idxmax()
    result = dataframe.loc[idx, [line,sell_row,month_row]].set_index(line).to_dict('index')
    return {k: {'Vendas': v[sell_row], 'Mês': v[month_row]} for k, v in result.items()}


def top_month(dataframe, month='Mes',line="Produto", sell_row='Vendas'):
    total_vendas_por_mes = dataframe.groupby(month)[sell_row].sum()

    highest_top_month = total_vendas_por_mes.idxmax()
    highest_sales = total_vendas_por_mes.max()

    print("Vendas totais por mês:")
    print(total_vendas_por_mes)
    print(f"\nO mês com o maior total de vendas é {highest_top_month}, com {highest_sales} vendas.")

    return total_vendas_por_mes, highest_top_month, highest_sales


def growth_rate(dataframe,product, month='Mes',line="Produto", sell_row='Vendas'):

    vendas = dataframe[dataframe[line] == product].set_index(month)[sell_row]
    growth = vendas.pct_change() * 100
    return growth    


overall_sellings = total_vendas(data)
linha_top_mes = prod_top_month(data)

print(overall_sellings)
print(linha_top_mes)
print(top_month(data))
growth_rate(data,'Eletrônicos')
graphic_yearly_measure(data, 'Eletrônicos', rotate_index=0,figsize_index=(12,6))
