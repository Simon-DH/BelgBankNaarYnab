sed 's/\r/\n/g' $1 | awk 'BEGIN { FS=";"; OFS=";"; print "Date", "Payee", "Memo", "Amount" } {if (NR!=1) {print $6, $15, $7, $9 }}' > KBCynab.csv

