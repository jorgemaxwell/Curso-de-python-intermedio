def run():
    my_list= [1,'hello',True,4.5]
    my_dict= {'firstname':'jorge',"lastname":'Barcasnegras'}

    super_list= [
        {'firstname':'Facundo',"lastname":'Garcia'},
        {'firstname':'Miguel',"lastname":'Torres'},
        {'firstname':'Pepe',"lastname":'Rodelo'},
        {'firstname':'Susana',"lastname":'Martinez'},
        {'firstname': 'jose',"lastname":'Garcia'},
        {'firstname':'Fredy',"lastname":'Vega'}
    ]

    super_dict= {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [-1,-2,0,1,2],
        'floating_nums': [1.1, 4.5, 6.4]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    
    for element in super_list:
        print(element)

    
if __name__ == "__main__":
    run()
