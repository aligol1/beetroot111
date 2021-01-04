def make_country(country, capital):
    country_dictation = {'country': country, 'capital': capital}
def print_dictat(d):
    print(d.values())
if __name__=="__main__":
    dat = make_country("Ukraine", "Kiev")
    print_dictat(dat)