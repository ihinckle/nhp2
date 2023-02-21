import csv

from src.classes.SoSLinkedList import SoSLinkedList
from src.constants import ID_STR, DELIVERY_STATUS_STR, Delivery_Statuses
from src.utils.getPackageDeliverBy import get_package_deliver_by


def get_packages():
    packages = []
    package_order = SoSLinkedList()
    with open('resources/Packages.csv') as csv_file:
        packages_stream = csv.reader(csv_file)
        headers = []
        packages.append(None)
        for row in packages_stream:
            if row[0] == ID_STR:
                headers = row
                continue
            package = {}
            for i in range(len(row)):
                package[headers[i]] = row[i]
            package[DELIVERY_STATUS_STR] = Delivery_Statuses.AT_HUB
            packages.append(package)
            deliver_package_by = get_package_deliver_by(package)
            if package_order.size == 0:
                package_order.add(package.get(ID_STR))
            elif not deliver_package_by:
                package_order.add(package.get(ID_STR))
            else:
                package_order.iterate()
                while package_order.cursor:
                    package_to_compare = packages[int(package_order.cursor.value)]
                    if not get_package_deliver_by(package_to_compare):
                        package_order.insert_before(package_order.cursor, package.get(ID_STR))
                        break
                    if deliver_package_by < get_package_deliver_by(package_to_compare):
                        package_order.insert_before(package_order.cursor, package.get(ID_STR))
                        break
                    package_order.next()
    return packages, package_order
