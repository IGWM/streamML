import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_time_dict():
    return {
        "2002-04-01": 0,
        "2002-05-01": 1,
        "2002-08-01": 2,
        "2002-09-01": 3,
        "2002-10-01": 4,
        "2002-11-01": 5,
        "2002-12-01": 6,
        "2003-01-01": 7,
        "2003-02-01": 8,
        "2003-03-01": 9,
        "2003-04-01": 10,
        "2003-05-01": 11,
        "2003-07-01": 12,
        "2003-08-01": 13,
        "2003-09-01": 14,
        "2003-10-01": 15,
        "2003-11-01": 16,
        "2003-12-01": 17,
        "2004-01-01": 18,
        "2004-02-01": 19,
        "2004-03-01": 20,
        "2004-04-01": 21,
        "2004-05-01": 22,
        "2004-06-01": 23,
        "2004-07-01": 24,
        "2004-08-01": 25,
        "2004-09-01": 26,
        "2004-10-01": 27,
        "2004-11-01": 28,
        "2004-12-01": 29,
        "2005-01-01": 30,
        "2005-02-01": 31,
        "2005-03-01": 32,
        "2005-04-01": 33,
        "2005-05-01": 34,
        "2005-06-01": 35,
        "2005-07-01": 36,
        "2005-08-01": 37,
        "2005-09-01": 38,
        "2005-10-01": 39,
        "2005-11-01": 40,
        "2005-12-01": 41,
        "2006-01-01": 42,
        "2006-02-01": 43,
        "2006-03-01": 44,
        "2006-04-01": 45,
        "2006-05-01": 46,
        "2006-06-01": 47,
        "2006-07-01": 48,
        "2006-08-01": 49,
        "2006-09-01": 50,
        "2006-10-01": 51,
        "2006-11-01": 52,
        "2006-12-01": 53,
        "2007-01-01": 54,
        "2007-02-01": 55,
        "2007-03-01": 56,
        "2007-04-01": 57,
        "2007-05-01": 58,
        "2007-06-01": 59,
        "2007-07-01": 60,
        "2007-08-01": 61,
        "2007-09-01": 62,
        "2007-10-01": 63,
        "2007-11-01": 64,
        "2007-12-01": 65,
        "2008-01-01": 66,
        "2008-02-01": 67,
        "2008-03-01": 68,
        "2008-04-01": 69,
        "2008-05-01": 70,
        "2008-06-01": 71,
        "2008-07-01": 72,
        "2008-08-01": 73,
        "2008-09-01": 74,
        "2008-10-01": 75,
        "2008-11-01": 76,
        "2008-12-01": 77,
        "2009-01-01": 78,
        "2009-02-01": 79,
        "2009-03-01": 80,
        "2009-04-01": 81,
        "2009-05-01": 82,
        "2009-06-01": 83,
        "2009-07-01": 84,
        "2009-08-01": 85,
        "2009-09-01": 86,
        "2009-10-01": 87,
        "2009-11-01": 88,
        "2009-12-01": 89,
        "2010-01-01": 90,
        "2010-02-01": 91,
        "2010-03-01": 92,
        "2010-04-01": 93,
        "2010-05-01": 94,
        "2010-06-01": 95,
        "2010-07-01": 96,
        "2010-08-01": 97,
        "2010-09-01": 98,
        "2010-10-01": 99,
        "2010-11-01": 100,
        "2010-12-01": 101,
        "2011-02-01": 102,
        "2011-03-01": 103,
        "2011-04-01": 104,
        "2011-05-01": 105,
        "2011-07-01": 106,
        "2011-08-01": 107,
        "2011-09-01": 108,
        "2011-10-01": 109,
        "2011-11-01": 110,
        "2012-01-01": 111,
        "2012-02-01": 112,
        "2012-03-01": 113,
        "2012-04-01": 114,
        "2012-06-01": 115,
        "2012-07-01": 116,
        "2012-08-01": 117,
        "2012-09-01": 118,
        "2012-11-01": 119,
        "2012-12-01": 120,
        "2013-01-01": 121,
        "2013-02-01": 122,
        "2013-04-01": 123,
        "2013-05-01": 124,
        "2013-06-01": 125,
        "2013-07-01": 126,
        "2013-10-01": 127,
        "2013-11-01": 128,
        "2013-12-01": 129,
        "2014-01-01": 130,
        "2014-03-01": 131,
        "2014-04-01": 132,
        "2014-05-01": 133,
        "2014-06-01": 134,
        "2014-08-01": 135,
        "2014-09-01": 136,
        "2014-10-01": 137,
        "2014-11-01": 138,
        "2015-01-01": 139,
        "2015-02-01": 140,
        "2015-03-01": 141,
        "2015-04-01": 142,
        "2015-07-01": 143,
        "2015-08-01": 144,
        "2015-09-01": 145,
        "2015-12-01": 146,
        "2016-01-01": 147,
        "2016-02-01": 148,
        "2016-03-01": 149,
        "2016-05-01": 150,
        "2016-06-01": 151,
        "2016-07-01": 152,
        "2016-08-01": 153,
        "2016-11-01": 154,
        "2016-12-01": 155,
        "2017-01-01": 156,
        "2017-03-01": 157,
        "2017-04-01": 158,
        "2017-05-01": 159,
        "2017-06-01": 160,
        "2018-06-01": 161,
        "2018-07-01": 162,
        "2018-10-01": 163,
        "2018-11-01": 164,
        "2018-12-01": 165,
        "2019-01-01": 166,
        "2019-02-01": 167,
        "2019-03-01": 168,
        "2019-04-01": 169,
        "2019-05-01": 170,
        "2019-06-01": 171,
        "2019-07-01": 172,
        "2019-08-01": 173,
        "2019-09-01": 174,
        "2019-10-01": 175,
        "2019-11-01": 176,
        "2019-12-01": 177,
        "2020-01-01": 178,
        "2020-02-01": 179,
        "2020-03-01": 180,
        "2020-04-01": 181,
        "2020-05-01": 182,
        "2020-06-01": 183,
        "2020-07-01": 184,
        "2020-08-01": 185,
        "2020-09-01": 186,
        "2020-10-01": 187,
        "2020-11-01": 188,
        "2020-12-01": 189,
    }


def load_scaler():
    # Load or define your scaler here
    scaler = StandardScaler()
    # Assuming you have a saved scaler, you would load it here
    # scaler = pickle.load(open('saved_models/scaler.pkl', 'rb'))
    return scaler