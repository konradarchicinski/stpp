import unittest
import stpp


class SpecialFunctionsTests(unittest.TestCase):
    def setUp(self):
        self.unit_square = [
            0.001, 0.005, 0.010, 0.025, 0.050, 0.100, 0.250, 0.500, 0.750,
            0.900, 0.950, 0.975, 0.990, 0.995, 0.999
        ]

    def test_erfinv(self):
        positives = [
            0.0008862271574665521, 0.004431163629370726, 0.008862501280950598,
            0.0221592995960528500, 0.044340387910005500, 0.088855990494257690,
            0.2253120550121781000, 0.476936276204469900, 0.813419847597618800,
            1.1630871536766743000, 1.385903824349677700, 1.584911068059480000,
            1.8213863677184485000, 1.984872612615532500, 2.326753765513515300
        ]
        negatives = [
            -0.0008862271574665521, -0.0044311636293707260,
            -0.0088625012809505980, -0.0221592995960528500,
            -0.0443403879100055000, -0.0888559904942576900,
            -0.2253120550121781000, -0.4769362762044699000,
            -0.8134198475976188000, -1.1630871536766743000,
            -1.3859038243496777000, -1.5849110680594800000,
            -1.8213863677184485000, -1.9848726126155325000,
            -2.3267537655135153000
        ]
        for i, number in enumerate(self.unit_square):
            self.assertEqual(
                stpp.erfinv(number),
                positives[i],
                msg=f"testing inverse error function for {number}")
            self.assertEqual(
                stpp.erfinv(-number),
                negatives[i],
                msg=f"testing inverse error function for {-number}")

    def test_betainc(self):
        params_pairs = [(0.20, 5.00), (0.14, 0.26), (0.20, 0.20), (5.00, 5.00),
                        (1.00, 1.00), (0.83, 0.35), (5.00, 0.20)]
        expected_betainc = [
            [
                0.37110992097223300, 0.51067173006673180, 0.58466985317566080,
                0.69539175756049120, 0.78606963597365350, 0.87547946232583550,
                0.96770924195657960, 0.99712861520155850, 0.99993028758815530,
                0.99999936590338830, 0.99999998087922700, 0.99999999941268550,
                0.99999999999404670, 0.99999999999981460, 0.99999999999999990
            ],
            [
                0.25892714714125680, 0.32448277984748420, 0.35771276370842070,
                0.40723665150155460, 0.44978999893091476, 0.49803561155998033,
                0.57535264097566270, 0.65580343458874560, 0.73117005487699420,
                0.79471714884827800, 0.83018974825661650, 0.85884217285976590,
                0.88906545080269210, 0.90744259457995850, 0.93913468230559990
            ],
            [
                0.13220129172927297, 0.18249959904813323, 0.20977769006771885,
                0.25248117764870187, 0.29102506644037396, 0.33668977824418944,
                0.41405551904012616, 0.49999999947195290, 0.58594448095987380,
                0.66331022175581060, 0.70897493355962600, 0.74751882235129800,
                0.79022230993228130, 0.81750040095186670, 0.86779870827072700
            ],
            [
                1.2558053968506e-13, 3.8722956458982e-10, 1.2185368569981e-08,
                1.1311777876004e-06, 3.3222207031818e-05, 0.00089092000010686,
                0.04892730711072058, 0.49999999999999970, 0.95107269288927940,
                0.99910907999989320, 0.99996677779296820, 0.99999886882221240,
                0.99999998781463140, 0.99999999961277040, 0.99999999999987440
            ],
            self.unit_square,
            [
                0.00124969446540248, 0.00475841455348372, 0.00847151477652627,
                0.01820531330291433, 0.03260992319758301, 0.05888485940530815,
                0.13261547609762006, 0.26218593780345510, 0.42959794549861620,
                0.58916898789535250, 0.67841352014930110, 0.74797295542165850,
                0.81724139831095450, 0.85664225235144080, 0.91839721924476370
            ],
            [
                5.9175454437008e-17, 1.8541838574308e-13, 5.9533306328348e-12,
                5.8731449661667e-10, 1.9120773012892e-08, 6.3409661169258e-07,
                6.9712411844762e-05, 0.00287138479844154, 0.03229075804342042,
                0.12452053767416393, 0.21393036402634558, 0.30460824243950880,
                0.41533014682433900, 0.48932826993326806, 0.62889007902776700
            ],
        ]

        for i, pair in enumerate(params_pairs):
            for j, number in enumerate(self.unit_square):
                self.assertAlmostEqual(
                    stpp.betainc(*pair, number),
                    expected_betainc[i][j],
                    msg=("testing beta incomplete function for "
                         f"{number} and {pair} parameters"))

    def test_gammainc(self):
        params = [0.5, 1.0, 5.0, 10.0]
        numbers = [
            0.0, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 15.0, 18.0, 19.0, 19.5,
            19.8, 19.9, 20.0
        ]
        expected_gammainc = [
            [
                0.00000000000000000, 0.34527915398142317, 0.47291074313446196,
                0.68268949213708590, 0.84270079294971510, 0.95449973610364150,
                0.99843459774199750, 0.99999225578356900, 0.99999995679536950,
                0.99999999802682470, 0.99999999929255370, 0.99999999957619450,
                0.99999999968831670, 0.99999999971865490, 0.99999999974603710
            ],
            [
                0.00000000000000000, 0.09516258196404044, 0.18126924692201815,
                0.39346934028736650, 0.63212055882855770, 0.86466471676338730,
                0.99326205300091450, 0.99995460007023750, 0.99999969409767950,
                0.99999998477002030, 0.99999999439720360, 0.99999999660173220,
                0.99999999748250120, 0.99999999772207290, 0.99999999793884640
            ],
            [
                0.00000000000000000, 7.6678016861893e-08, 2.2581905529578e-06,
                0.00017211562995584, 0.00365984682734371, 0.05265301734371113,
                0.55950671493478790, 0.97074731192303890, 0.99914335878922470,
                0.99991582390195100, 0.99996204829108100, 0.99997461146147370,
                0.99998007519244060, 0.99998162471844120, 0.99998305525606990
            ],
            [
                0.00000000000000000, 2.5163478067703e-17, 2.3530687525611e-14,
                1.7096700293489e-10, 1.1142547833872e-07, 4.6498075017264e-05,
                0.03182805730620481, 0.54207028552814780, 0.93014633930059010,
                0.98461890273941070, 0.99114441614387480, 0.99333261337076100,
                0.99438985665488280, 0.99470563768019060, 0.99500458769169240
            ],
        ]

        for i, param in enumerate(params):
            for j, number in enumerate(numbers):
                self.assertAlmostEqual(
                    stpp.gammainc(param, number),
                    expected_gammainc[i][j],
                    msg=("testing gamma incomplete function for "
                         f"{number} and {param} parameter"))


if __name__ == "__main__":
    unittest.main()
