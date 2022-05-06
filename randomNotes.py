<html>
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>

<py-script> print('Now you can!') </py-script>
<py-script>  3+4 </py-script>
<py-script>  for i in range(1,10):
                print(i, " hello KK!")
 </py-script>
</html>



data = censusdata.download('acs5', 2015,
            censusdata.censusgeo([('state', '36'),
                                  ('county', '081'),
                                  ('block group', '*')]),
           ['B23025_001E', 'B23025_002E', 'B23025_003E',
            'B23025_004E', 'B23025_005E',
            'B23025_006E', 'B23025_007E'])


data3 = censusdata.download('acs5', 2019,
    censusdata.censusgeo([('state', '12'),
                            ('county', '*'),
                            ('tract', '*')]),
    ['B09001_004E', 'B14003_022E', 'B14003_050E',
     'B19119_004E', 'B14006_004E'])


     with pd.option_context('display.max_colwidth', None)
     display(df)

     pd.set_option('display.max_colwidth', None)
