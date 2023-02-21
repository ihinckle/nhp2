from enum import Enum

DEADLINE_STR = 'Delivery Deadline'
DELIVERY_STATUS_STR = 'Delivery Status'
EOD = 'EOD'
ID_STR = 'ID'
TIME_FORMAT = '%I:%M %p'

Delivery_Statuses = Enum('Delivery_Statuses', ['AT_HUB', 'OUT_FOR_DELIVERY', 'DELIVERED'])
