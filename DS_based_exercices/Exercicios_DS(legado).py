import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('dados_aleatorios.csv')

def total_vendas(dataframe, linha="Produto", colum_vendas='Vendas'):
    total_vendas= {}
    proviso = 0

    for vendas in dataframe[linha]:
        for _, a in dataframe[dataframe[linha] == vendas].iterrows():
            proviso += a[colum_vendas]
            total_vendas[str(vendas)] = {'total de vendas': proviso,      
            }
        proviso = 0

    return total_vendas



def graphic_yearly_measure(dataframe, product,rotate_index=0,figsize_index=(5,5), month_row='Mes',line="Produto", sell_row='Vendas'):
    meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',       
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro']
    Valendas = {}
    vendas = []

    for prod in dataframe[line].unique():
        organizado_= dataframe[dataframe[line] == prod]

        if prod not in Valendas:
            Valendas[prod] = {}

        for _,xaxa in organizado_.iterrows():
            Valendas[prod][xaxa[month_row]] = xaxa[sell_row]

    for mes in meses:
        if mes in Valendas[product]:
            vendas.append(Valendas[product][mes])
        else:
            vendas.append(0)
    plt.figure(figsize=figsize_index)
    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.bar(meses, vendas, color='orange')
    plt.title(f'Venda de {product} ao longo do ano')
    plt.xticks(rotation=rotate_index)


    plt.tight_layout()
    plt.show()



def prod_top_month(dataframe, month_row='Mes',line="Produto", sell_row='Vendas'):
    prod_top_month = {}
    for prod in dataframe[line].unique():
        selling_top = 0
        for _, top_vendas in dataframe[dataframe[line]== prod].iterrows():
            if top_vendas.loc[sell_row] > selling_top:
                selling_top = top_vendas.loc[sell_row]
                product = top_vendas.loc[line]
                months = top_vendas.loc[month_row]
        prod_top_month[str(product)] = {'Vendas': selling_top,
                                'Mês': months
                                    }
    return prod_top_month


def top_month(dataframe, month='Mes',line="Produto", sell_row='Vendas'):
    total_vendas_por_mes = dataframe.groupby(month)[sell_row].sum()

    highest_top_month = total_vendas_por_mes.idxmax()
    highest_sales = total_vendas_por_mes.max()

    print("Vendas totais por mês:")
    print(total_vendas_por_mes)
    print(f"\nO mês com o maior total de vendas é {highest_top_month}, com {highest_sales} vendas.")

    return total_vendas_por_mes, highest_top_month, highest_sales


def growth_rate(dataframe,product, month='Mes',line="Produto", sell_row='Vendas'):
    a = -1
    vendas = []
    for _,prod in dataframe[dataframe[line] == product].iterrows():
        vendas.append(prod[sell_row])
    while a <=len(vendas):    
        a += 1
        b = a +1
        try:
            print(vendas[a:a+2] )

            # print(f"{((vendas[b] - vendas[a])/vendas[a] )* 100:.2f}%")
            print(f"{((vendas[b] - vendas[a])/vendas[a] )* 100:.2f}%"  ) 
        except IndexError:
            print('fim da lista')
            break                  


overall_sellings = total_vendas(data)

linha_top_mes = prod_top_month(data)

# total_vendas_por_mes, highest_top_month, highest_sales = top_month(data)


print(overall_sellings)
print(linha_top_mes)
print(top_month(data))
growth_rate(data,'Eletrônicos')

graphic_yearly_measure(data, 'Eletrônicos', rotate_index=0,figsize_index=(12,6))


