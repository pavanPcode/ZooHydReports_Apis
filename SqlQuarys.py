insertSipetransaction = """
        INSERT INTO ZooSwipeTransactions (superId, BID, ticketType, BRN, GATE, availableAdultEntryCount,
                                       totalAdultEntryCount, bookingDate, createdOn, isactive)
        VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}', '{8}', 1)
        """

insertHelathcheck = """INSERT INTO ZooHealthStatus (typeid, message, gate, ErrorMessage,createdOn,superid,GateType)
VALUES ({0}, '{1}', '{2}', '{3}',DATE_ADD(UTC_TIMESTAMP(), INTERVAL '5:30' HOUR_MINUTE),{4},'{5}');
"""