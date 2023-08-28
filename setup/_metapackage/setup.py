import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-purchase",
    description="Meta package for open-synergy-ssi-purchase Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_purchase',
        'odoo14-addon-ssi_purchase_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
