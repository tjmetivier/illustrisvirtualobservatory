#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
                                        Illustris Virtual Observatory,
                                     Tyler Metivier, tylerphys@uconn.edu
                                          University of Connecticut

                                        NASA CT Space Grant Consortium                              (Tyler's funding)
                                  Adapted from Sunpy module by Dr. Torrey 2015
"""


import numpy as np
import os
import sys
sys.path.append('../..')
import sunpy__load as sunpy__load
import sunpy__plot as sunpy__plot

os.system('cls')

print(r"""


 ____________________________________________________________________________________________________________
/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/
  ██╗██╗     ██╗     ██╗  *██╗███████╗████████╗██████╗ ██╗███████╗      *               *               *
  ██║██║ *   ██║     ██║ * ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝                          *
  ██║██║     ██║     ██║   ██║███████╗   ██║ * ██████╔╝██║███████╗*              *
  ██║██║     ██║  *  ██║   ██║╚════██║ * ██║   ██╔══██╗██║╚════██║       *         *            **
  ██║███████╗███████╗╚██████╔╝███████║   ██║   ██║  ██║██║███████║                 \│/  *                   ,-.
  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝          *     - o -        *           / \  `.  __..-,O
██╗*  ██╗██╗██████╗ ████████╗██╗ * ██╗ █████╗ ██╗    *                *            /│\                *   :   \ --''_..-'.'
██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║                 *         *             *               |    . .-' `. '.
██║ * ██║██║██████╔╝   ██║   ██║   ██║███████║██║    *       *                    *                       :     .     .`.'
╚██╗ ██╔╝██║██╔══██╗ * ██║   ██║   ██║██╔══██║██║                          *                               \     `.  /  ..
 ╚████╔╝ ██║██║  ██║   ██║  *╚██████╔╝██║  ██║███████╗       *                       *         *        *   \      `.   ' .
  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝                   *                                   `,       `.   \
    *    ██████╗ ██████╗ ███████╗███████╗██████╗ ██╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ ██╗   ██╗       ,|,`.        `-.\
        ██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝      '.||  ``-...__..-`
*       ██║   ██║██████╔╝███████╗█████╗  ██████╔╝██║   ██║███████║   ██║   ██║   ██║██████╔╝ ╚████╔╝        |  |
        ██║   ██║██╔══██╗╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝         |__|
*       ╚██████╔╝██████╔╝███████║███████╗██║  ██║ ╚████╔╝ ██║  ██║   ██║   ╚██████╔╝██║  ██║   ██║          /||\
                            *                        *                  *                                  //||\\
*         **       *                    *                           *           *           *             // || \\
    *                *          *                    *     *                         *                 __//__||__\\__
        *        *               *            *                   *               *              *    '--------------'
 ____________________________________________________________________________________________________________
/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/

""")
start = input(r"""

       \│/           ┌─┐┬─┐┌─┐┌─┐┌─┐  ╔═╗╔╗╔╔╦╗╔═╗╦═╗  ┌┬┐┌─┐  ┌─┐┌─┐┌┐┌┌┬┐┬┌┐┌┬ ┬┌─┐           \│/
       ─ ──────────  ├─┘├┬┘├┤ └─┐└─┐  ║╣ ║║║ ║ ║╣ ╠╦╝   │ │ │  │  │ ││││ │ │││││ │├┤   ────────── ─
       /│\           ┴  ┴└─└─┘└─┘└─┘  ╚═╝╝╚╝ ╩ ╚═╝╩╚═   ┴ └─┘  └─┘└─┘┘└┘ ┴ ┴┘└┘└─┘└─┘           /│\

                                                                                                        4-26-2019
""")

os.system('cls')



my_api = "a4385a1f5eac5c06e2e2c1f45eebb4d3"  # This is my (T.M.) API

sim_vers = 2
if sim_vers == 1:
    dl_base = 'http://www.illustris-project.org'
elif sim_vers == 2:
    dl_base = 'http://www.tng-project.org'
    my_api = "e5a4933eb4eb2b11ec588ac67222b6ee"
else:
    print("Sorry, that's not an option")



try:
    try:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i10', 'f8')})
    except TypeError:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i8', 'f8')})
except IOError:
    os.system("wget " + dl_base + "/files/directory_catalog_135.txt")
    try:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i10', 'f8')})
    except TypeError:
        catalog = np.loadtxt('directory_catalog_135.txt',
                             dtype={'names': ('subdirs', 'galaxy_numbers', 'galaxy_masses'),
                                    'formats': ('S3', 'i8', 'f8')})
all_subdirs = catalog['subdirs']
all_galnrs = catalog['galaxy_numbers']

"""


    Below is where one can change any common arguments in order to customize your output images.



"""
common_args = {
    # default option = False, turn on one-by-one
    'add_background':       True,
    'add_noise':            True,
    'add_psf':              True,
    'rebin_phys':           True,
    'resize_rp':            False,
    'rebin_gz':             False,           # always FALSE - only on for Galaxy Zoo
    'scale_min':            1e-10,          # was 1e-4
    'lupton_alpha':         2e-12,          # was 1e-4
    'lupton_Q':             10,             # was ~100
    'pixelsize_arcsec':     0.06,           # SDSS - 0.24 native hst - .13, dithered - 0.06
    'psf_fwhm_arcsec':      0.16,            # SDSS - 1.3
    'sn_limit':             29.0,
    'sky_sig':              None,           #
    'redshift':             0.01,           #
    'b_fac':                1.0,
    'g_fac':                1.0,
    'r_fac':                1.0,
    'camera':               1,
    'seed_boost':           1.0,
    'save_fits':            True,
    'jwst':		            False
}

for index, galnr in enumerate(all_galnrs[:1]):
    os.system('cls')
    galnr = input('''
____________________________________________________________________________________________________________

                                    Please enter the galaxy ID number:
                                    ''')
    print("""
____________________________________________________________________________________________________________
                                    You chose galaxy""", galnr)

                                    # if IllustrisTNG has broadband fits files at some point, the below feature will be added


    if sim_vers == 2:                                                                               # This is the Illustris TNG API
        snapshot = "/snapshots/135"
        cmd = 'wget --content-disposition --header="API-Key: ' + my_api + '" "' + dl_base + \
            '/api/Illustris-1'+ snapshot +'/subhalos/' + str(galnr) +  \
            '/stellar_mocks/broadband.fits"'
    elif sim_vers ==1:                                                                              # This is the orig. Illustris API (USE)
        snapshot = "/snapshots/135"
        cmd = 'wget --content-disposition --header="API-Key: ' + my_api + '" "' + dl_base + \
            '/api/Illustris-1'+ snapshot +'/subhalos/' + str(galnr) +  \
            '/stellar_mocks/broadband.fits"'
if(not (os.path.isfile("./broadband_" + str(galnr) + ".fits"))):
    os.system(cmd)
filename = "./broadband_" + str(galnr) + ".fits"


tele = input('''
____________________________________________________________________________________________________________
                              ┌─┐┌─┐┬  ┌─┐┌─┐┌┬┐  ┌─┐┌┐┌  ┬┌┐┌┌─┐┌┬┐┬─┐┬ ┬┌┬┐┌─┐┌┐┌┌┬┐
            ──────────────────└─┐├┤ │  ├┤ │   │   ├─┤│││  ││││└─┐ │ ├┬┘│ ││││├┤ │││ │──────────────────
                              └─┘└─┘┴─┘└─┘└─┘ ┴   ┴ ┴┘└┘  ┴┘└┘└─┘ ┴ ┴└─└─┘┴ ┴└─┘┘└┘ ┴

                Hubble Space Telescope (1)          or            Sloan Digital Sky Survey (2)

		       	     	       	 James Webb Space Telescope (3)

                                              (enter 1, 2, or 3)
                                                     :''')
redshift = np.float64(input("""
____________________________________________________________________________________________________________
                               ┌─┐┬ ┬┌─┐┌─┐┌─┐┌─┐  ┌─┐  ┬─┐┌─┐┌┬┐┌─┐┬ ┬┬┌─┐┌┬┐
                ───────────────│  ├─┤│ ││ │└─┐├┤   ├─┤  ├┬┘├┤  ││└─┐├─┤│├┤  │───────────────
                               └─┘┴ ┴└─┘└─┘└─┘└─┘  ┴ ┴  ┴└─└─┘─┴┘└─┘┴ ┴┴└   ┴

                                                     :"""))
if redshift == float(0):
    common_args['redshift'] = float(0.001)
else:
    common_args['redshift'] = redshift
if tele == '2':
    common_args['pixelsize_arcsec'] = 0.24
    common_args['psf_fwhm_arcsec'] = 1.3
    sunpy__plot.plot_synthetic_sdss_gri(
        filename, savefile='./synthetic_sdss' + str(galnr) + '.png', **common_args)
    x = 'Sloan Digital Sky Survey'

elif tele == '1':
    sunpy__plot.plot_synthetic_hst(                                                     #plot_synthetic_hst is the main funcion
        filename, savefile='./synthetic_hst' + str(galnr) + '.png', **common_args)
    x = 'Hubble Space Telescope'
elif tele == '3':
    common_args['pixelsize_arcsec'] = 0.031
    common_args['psf_fwhm_arcsec'] = 0.064
    common_args['jwst'] = True
    n_pixels_galaxy_zoo = 2048
    sunpy__plot.plot_synthetic_jwst(
        filename, savefile='./synthetic_jwst' + str(galnr) + '.png',**common_args)
    x = 'James Webb Space Telescope'
else:
    print('I do not understand what you mean')


print('''
_____________________________________________________________________________________________________________________
''')
print('Your ' + str(x) + ' observations at redshift ' +
      str(redshift) + ' for galaxy ' + str(galnr) + ' are complete,')
input('''
_____________________________________________________________________________________________________________________
''')

os.system('cls')

input(r"""
_____________________________________________________________________________________________________________________
                               ╦ ╦╔═╗┌─┐┌┐┌┌┐┌  ╔═╗┌─┐┌┬┐┬─┐┌─┐┌─┐┬ ┬┬ ┬┌─┐┬┌─┐┌─┐
                               ║ ║║  │ │││││││  ╠═╣└─┐ │ ├┬┘│ │├─┘├─┤└┬┘└─┐││  └─┐
                               ╚═╝╚═╝└─┘┘└┘┘└┘  ╩ ╩└─┘ ┴ ┴└─└─┘┴  ┴ ┴ ┴ └─┘┴└─┘└─┘
                        ╦ ╦┬ ┬┬┌┬┐┌─┐┬┌─┌─┐┬─┐  ╦═╗┌─┐┌─┐┌─┐┌─┐┬─┐┌─┐┬ ┬  ╔═╗┬─┐┌─┐┬ ┬┌─┐
                        ║║║├─┤│ │ ├─┤├┴┐├┤ ├┬┘  ╠╦╝├┤ └─┐├┤ ├─┤├┬┘│  ├─┤  ║ ╦├┬┘│ ││ │├─┘
                        ╚╩╝┴ ┴┴ ┴ ┴ ┴┴ ┴└─┘┴└─  ╩╚═└─┘└─┘└─┘┴ ┴┴└─└─┘┴ ┴  ╚═╝┴└─└─┘└─┘┴
                                       ╔╗╔╔═╗╔═╗╔═╗  ╔═╗╔╦╗  ╔═╗ ╔═╗ ╔═╗
                                       ║║║╠═╣╚═╗╠═╣  ║   ║   ╚═╗ ║ ╦ ║
                                       ╝╚╝╩ ╩╚═╝╩ ╩  ╚═╝ ╩   ╚═╝.╚═╝.╚═╝.

                                                 THANK YOU

                                        (press return to end program)
____________________________________________________________________________________________________________________
""")

# THANK YOU :)
# FEEL FREE TO REACH OUT AND CONTACT ME FOR ANY REASON : tylerphys@uconn.edu, tyler.metivier@gmail.com

os.system('cls')

exit()
