#!/bin/bash
limit=250000
offset=0
endpoint="https://data.cityofnewyork.us/resource/pvqr-7yc4.json"
combinedFilename="data.json"
totalRowCount=0
echo "[" > "$combinedFilename"
firstChunk=true
while :; do
    tempFilename="temp_chunk.json"
    curl "${endpoint}?\$limit=${limit}&\$offset=${offset}" -o "$tempFilename"
    rowCount=$(jq '. | length' "$tempFilename")
    totalRowCount=$((totalRowCount + rowCount))
    if $firstChunk ; then
        firstChunk=false
    else
        sed -i '$ s/.$//' "$combinedFilename"
        echo -n "," >> "$combinedFilename"
        tail -c +2 "$tempFilename" >> "$combinedFilename"
    fi
    if [ "$totalRowCount" -ge 7005000 ]; then break; fi
    if [ "$rowCount" -lt "$limit" ]; then break; fi
    offset=$((offset + limit))
done
echo "]" >> "$combinedFilename"
rm -f "temp_chunk.json"
echo "All data combined into $combinedFilename"