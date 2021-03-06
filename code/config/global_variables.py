URLS_FUNDS_CA = ['https://www.boursorama.com/bourse/opcvm/cours/0P00016DRV/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001AMLS/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P00016LLM/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P00016P31/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-828959/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-828841/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P00011IWP/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-356460/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0000TIK4/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001HV65/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0000XWUI/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-442076/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001CC08/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-984095/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0000YNF8/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-809773/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-806992/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-546993/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001DH3M/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001DWME/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001EOO3/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001H3VS/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001HET2/',
                 'https://www.boursorama.com/bourse/opcvm/cours/MP-828192/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0000W8CR/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P00016DVT/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001DH3L/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001DWMF/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001EONQ/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001FFVK/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P0001HETC/',
                 'https://www.boursorama.com/bourse/opcvm/cours/0P00011RIT/'
                 ]

nb_page = 15
ALL_PAGES = [
    f'https://www.boursorama.com/bourse/actions/cotations/page-{i}?quotation_az_filter%5Bmarket%5D=SRD&quotation_az_filter%5Bletter%5D=&quotation_az_filter%5BpeaEligibility%5D=1&quotation_az_filter%5Bfilter%5D=&pagination_1447025609='
    for i in range(1, nb_page + 1)
]

URLS_RECOMMENDED_ASSETS = [
    f"https://www.boursorama.com/bourse/actions/consensus/recommandations-paris/page-{i}?national_market_filter%5Bmarket%5D=1rPCAC&national_market_filter%5Bsector%5D=&national_market_filter%5Banalysts%5D=10&national_market_filter%5Bperiod%5D=2021&national_market_filter%5Bfilter%5D=&sortColumn=consPotential&orderAsc=0"
    for i in range(1, 4)
]
