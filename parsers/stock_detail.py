from bs4 import BeautifulSoup
def retireve_bse_nse_data(div_soup):
    dict = {}
    f = open("nchrtprc.txt", "w")
    bsestock = find_val(div_soup, 'div', 'id', 'content_bse')
    bsetick = find_val(bsestock, 'div', 'id', 'Bse_Prc_tick_div')
    bsetick_span = find_val(bsetick, 'span', 'id', 'Bse_Prc_tick')
    dict['bse']['price'] = bsetick_span.strong.text
    f.write(bsetick_span.strong.text)
    f.close()
    print(f"dict is {dict}")
    return dict    

def find_val(html, element, type, value):
    child = ""
    if(type == 'class'):
        child = html.find(element, class_ = value)
    elif(type == 'id'):
        child = html.find(element, id=value)
    return child
