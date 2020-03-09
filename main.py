from astroquery.mast import Catalogs, Observations

# Read in your list of TIC IDs, for this example I'll just have
# them in an array already.
tids = ['2760710', '9006668', '9725627', '9727392', '12421862', '12423815']
for tid in tids:
    # This query will get all the TESS mission data for this TIC ID.
    obsTable = Observations.query_criteria(obs_collection="TESS", target_name=tid)
    # This gets all the products for the returned set of Sectors, e.g.,
    # light curves, target pixel files, DV reports, etc..
    data_products = Observations.get_product_list(obsTable)
    # This will filter so that only the light curve files are left.
    light_curves = Observations.filter_products(data_products, productSubGroupDescription="LC")
    # Let's download these files.
    Observations.download_products(light_curves)