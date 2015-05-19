from bs4 import BeautifulSoup
import urllib2

# List of S&P500 company stock symbols
stocks = {"MMM","ABT","ABBV","ACN","ACE","ACT","ADBE","ADT","AES","AET","AMG","AFL","A","GAS","APD","ARG","AKAM","AA","ALXN","ALLE","AGN","ADS","ALL","ALTR","MO","AMZN","AEE","AEP","AXP","AIG","AMT","AMP","ABC","AME","AMGN","APH","APC","ADI","AON","APA","AIV","AAPL","AMAT","ADM","AIZ","T","ADSK","ADP","AN","AZO","AVGO","AVB","AVY","AVP","BHI","BLL","BAC","BK","BCR","BAX","BBT","BDX","BBBY","BMS","BRK-B","BBY","BIIB","BLK","BA","BWA","BXP","BSX","BMY","BRCM","BF-B","CHRW","CA","CVC","COG","CAM","CPB","COF","CAH","CFN","KMX","CCL","CAT","CBG","CBS","CELG","CNP","CTL","CERN","CF","CHK","CVX","CMG","CB","CI","XEC","CINF","CTAS","CSCO","C","CTXS","CLX","CME","CMS","COH","KO","CCE","CTSH","CL","CMCSA","CMA","CSC","CAG","COP","CNX","ED","STZ","GLW","COST","COV","CCI","CSX","CMI","CVS","DHI","DHR","DRI","DVA","DE","DLPH","DAL","DNR","XRAY","DVN","DO","DTV","DFS","DISCA","DG","DLTR","D","DOV","DOW","DPS","DTE","DD","DUK","DNB","ETFC","EMN","ETN","EBAY","ECL","EIX","EW","EA","EMC","EMR","ESV","ETR","EOG","EQT","EFX","EQR","ESS","EL","EXC","EXPE","EXPD","ESRX","XOM","FFIV","FB","FDO","FAST","FDX","FIS","FITB","FSLR","FE","FISV","FLIR","FLS","FLR","FMC","FTI","F","FOSL","BEN","FCX","FTR","GME","GCI","GPS","GRMN","GM","GD","GE","GGP","GIS","GPC","GNW","GILD","GS","GT","GOOG","GWW","HAL","HOG","HAR","HRS","HIG","HAS","HCP","HCN","HP","HSY","HES","HPQ","HD","HON","HRL","HSP","HST","HCBK","HUM","HBAN","ITW","IR","TEG","INTC","ICE","IBM","IFF","IP","IPG","INTU","ISRG","IVZ","IRM","JBL","JEC","JNJ","JCI","JPM","JNPR","KSU","K","GMCR","KEY","KMB","KIM","KMI","KLAC","KSS","KRFT","KR","LB","LLL","LH","LRCX","LM","LEG","LEN","LUK","LLY","LNC","LLTC","LMT","L","LO","LOW","LYB","MTB","MAC","M","MNK","MRO","MPC","MAR","MMC","MLM","MAS","MA","MAT","MKC","MCD","MHFI","MCK","MJN","MWV","MDT","MRK","MET","KORS","MCHP","MU","MSFT","MHK","TAP","MDLZ","MON","MNST","MCO","MS","MOS","MSI","MUR","MYL","NBR","NDAQ","NOV","NAVI","NTAP","NFLX","NWL","NFX","NEM","NWSA","NEE","NLSN","NKE","NI","NE","NBL","JWN","NSC","NU","NTRS","NOC","NRG","NUE","NVDA","ORLY","OXY","OMC","OKE","ORCL","OI","PCAR","PLL","PH","PDCO","PAYX","PNR","PBCT","POM","PEP","PKI","PRGO","PETM","PFE","PCG","PM","PSX","PNW","PXD","PBI","PCL","PNC","PPG","PPL","PX","PCP","PCLN","PFG","PG","PGR","PLD","PRU","PSA","PEG","PHM","PVH","QEP","QCOM","PWR","DGX","RL","RRC","RTN","RHT","REGN","RF","RSG","RAI","RHI","ROK","COL","ROP","ROST","R","SWY","CRM","SNDK","SCG","SLB","SCHW","SNI","STX","SEE","SRE","SHW","SIAL","SPG","SJM","SNA","SO","LUV","SWN","SE","STJ","SWK","SPLS","SBUX","HOT","STT","SRCL","SYK","STI","SYMC","SYY","TROW","TGT","TEL","TE","THC","TDC","TSO","TXN","TXT","TMO","TIF","TWX","TWC","TJX","TMK","TSS","TSCO","RIG","TRV","TRIP","FOXA","TSN","USB","UA","UNP","UPS","URI","UTX","UNH","UHS","UNM","URBN","VLO","VAR","VTR","VRSN","VZ","VRTX","VFC","VIAB","V","VNO","VMC","WMT","WAG","DIS","WM","WAT","WLP","WFC","WDC","WU","WY","WHR","WFM","WMB","WIN","WEC","WYN","WYNN","XEL","XRX","XLNX","XL","XYL","YHOO","YUM","ZMH","ZION","ZTS"};
base_url = 'http://finance.yahoo.com/q/it?s=';

#Iterates over each stock, parses their html tree and finds if there are any insider trades
#reported for today
for company in stocks:
    response = urllib2.urlopen(base_url+company)
    html = response.read()
    soup = BeautifulSoup(html)
    
    
    #Will find transactions here
    #for link in soup.find_all('a'):
    #S = link.get('href')
    
