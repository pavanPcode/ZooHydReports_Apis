insertSipetransaction = """
        INSERT INTO ZooSwipeTransactions (superId, BID, ticketType, BRN, GATE, availableAdultEntryCount,
                                       totalAdultEntryCount, bookingDate, createdOn, isactive,GATETYPE)
        VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}', '{8}', 1,'{9}')
        """

insertHelathcheck = """INSERT INTO ZooHealthStatus (typeid, message, gate, ErrorMessage,createdOn,superid,GateType)
VALUES ({0}, '{1}', '{2}', '{3}',DATE_ADD(UTC_TIMESTAMP(), INTERVAL '5:30' HOUR_MINUTE),{4},'{5}');
"""


gethealthstatusquary = """select * from zoohealthstatus where typeid = {0} 
and gate = {1} and 
{2} and GATETYPE = {3}"""

getSwipetransactionquary = """select * from zooswipetransactions where superid = superid and bid = {0} and 
tickettype = {1} and gate= {2} and gatetype = {3}
and bookingdate = {4};"""