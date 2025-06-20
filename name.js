
const url = 'https://clearoneadvantage.lightning.force.com/aura?r=98&aura.ListUi.postListRecordsByName=1';

const headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'https://clearoneadvantage.lightning.force.com',
    'Referer': 'https://clearoneadvantage.lightning.force.com/lightning/o/Opportunity/list?filterName=Default_Opportunity_Pipeline',
    'User-Agent': navigator.userAgent,
    'Cookie': 'CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; inst=APP_Ud; clientSrc=149.88.25.130; BrowserId=eRxBShz3EfCYkG2TGYWP7g; sid=00D4x000003yZoM!AQEAQJG6Yt_k5kwjQLanxt63FQgCfz2LHyUTFMbhEaCPrM4lgpzEhQFcQUKSsus_O1sbKuyW7k7Jf.dxEW973NGtaOcwrTyR; sid_Client=d0000087bKsx000003yZoM'
};

// El cuerpo de la solicitud (payload), codificado como formulario
const body = new URLSearchParams({
    message: JSON.stringify({
        actions: [
            {
                id: "18784;a",
                descriptor: "aura://ListUiController/ACTION$postListRecordsByName",
                callingDescriptor: "UNKNOWN",
                params: {
                    objectApiName: "Opportunity",
                    listViewApiName: "Default_Opportunity_Pipeline",
                    listRecordsQuery: {
                        fields: [
                            "Opportunity.Id",
                            "Opportunity.Name",
                            "Opportunity.Id",
                            "Opportunity.Applicant_State_Code__c",
                            "Opportunity.Owner.Name",
                            "Opportunity.OwnerId",
                            "Opportunity.Approx_Debt__c",
                            "Opportunity.CreatedDate",
                            "Opportunity.StageName",
                            "Opportunity.Sub_Stage__c",
                            "Opportunity.Marketing_Vendor_ID__c",
                            "Opportunity.Legal_Protection__c",
                            "Opportunity.Legal_Protection_Fees_Formula__c",
                            "Opportunity.Marketing_Vendor__r.Name",
                            "Opportunity.Marketing_Vendor__c",
                            "Opportunity.Processor__r.Name",
                            "Opportunity.Processor__c"
                        ],
                        optionalFields: ["Opportunity.StageName", "Opportunity.ForecastCategoryName", "Opportunity.Probability"],
                        pageSize: 50,
                        sortBy: ["Opportunity.CreatedDate"]
                    }
                }
            }
        ]
    }),
    'aura.context': JSON.stringify({
        mode: "PROD",
        fwuid: "QVctNlNJa216UjhqVnlObWs4a21Bd2g5TGxiTHU3MEQ5RnBMM0VzVXc1cmcxMS4zMjc2OC4z",
        app: "one:one",
        loaded: {
            "APPLICATION@markup://one:one": "3741_e8jTwyKShfsfFm38joU73w"
        },
        dn: [],
        globals: {
            density: "VIEW_TWO",
            appContextId: "06m4x000000iaGCAAY"
        },
        uad: true
    }),
    'aura.pageURI': '/lightning/o/Opportunity/list?filterName=Default_Opportunity_Pipeline',
    'aura.token': 'eyJub25jZSI6IlRWNUZqMkRONGFEZmF3Q1hMMFRWcUpFcFJYVGs5TS02OE9fZjNEM1lua01cdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFVkMDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHVWQwMDAwMDAwMDAxXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3NDkxNDEyNTE4OTAsImV4cCI6MH0=..dNbdy2C0C48uoB_RcHQZ2ddeZTCPD882jX5BSSu3Brs='
});

fetch(url, {
    method: 'POST',
    headers: headers,
    body: body,
    credentials: 'include'
})
    .then(response => response.json())
    .then(data => {

        const firstRecord = data.actions[0].returnValue.records[0];

// Acceder a 'Name'
        const name = firstRecord.fields.Name.value || firstRecord.fields.Name.displayValue;

// Acceder a 'Owner' (el nombre del usuario)
        const owner = firstRecord.fields.Owner.value.fields.Name.value;
        const Id = firstRecord.fields.Id.value || firstRecord.fields.Id.displayValue;
        console.log(name)

        console.log(owner)
        console.log(Id)

        // Hacer peticion aqui POST USANDO EL ID


    })
    .catch(error => {
        console.error('Error:', error);
    });

const dateSearchPhone = "6/5/2025";
const url = 'https://clearoneadvantage.lightning.force.com/aura?r=98&aura.ListUi.postListRecordsByName=1';

const headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'https://clearoneadvantage.lightning.force.com',
    'Referer': 'https://clearoneadvantage.lightning.force.com/lightning/o/Opportunity/list?filterName=Default_Opportunity_Pipeline',
    'User-Agent': navigator.userAgent,
    'Cookie': 'CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; inst=APP_Ud; clientSrc=149.88.25.130; BrowserId=eRxBShz3EfCYkG2TGYWP7g; sid=00D4x000003yZoM!AQEAQJG6Yt_k5kwjQLanxt63FQgCfz2LHyUTFMbhEaCPrM4lgpzEhQFcQUKSsus_O1sbKuyW7k7Jf.dxEW973NGtaOcwrTyR; sid_Client=d0000087bKsx000003yZoM'
};

const token = 'eyJub25jZSI6IlRWNUZqMkRONGFEZmF3Q1hMMFRWcUpFcFJYVGs5TS02OE9fZjNEM1lua01cdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRFVkMDAwMDAwMDAwMVwiLFwidlwiOlwiMDJHVWQwMDAwMDAwMDAxXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE3NDkxNDEyNTE4OTAsImV4cCI6MH0=..dNbdy2C0C48uoB_RcHQZ2ddeZTCPD882jX5BSSu3Brs='; // 🔐 Usa tu token real
const fwuid = 'QVctNlNJa216UjhqVnlObWs4a21Bd2g5TGxiTHU3MEQ5RnBMM0VzVXc1cmcxMS4zMjc2OC4z';

const body = new URLSearchParams({
    message: JSON.stringify({
        actions: [{"id":"10801;a","descriptor":"aura://ListUiController/ACTION$postListRecordsByName","callingDescriptor":"UNKNOWN","params":{"objectApiName":"Opportunity","listViewApiName":"Default_Opportunity_Pipeline","listRecordsQuery":{"fields":["Opportunity.Id","Opportunity.Name","Opportunity.Id","Opportunity.Applicant_State_Code__c","Opportunity.Owner.Name","Opportunity.OwnerId","Opportunity.Approx_Debt__c","Opportunity.CreatedDate","Opportunity.StageName","Opportunity.Sub_Stage__c","Opportunity.Marketing_Vendor_ID__c","Opportunity.Legal_Protection__c","Opportunity.Legal_Protection_Fees_Formula__c","Opportunity.Marketing_Vendor__r.Name","Opportunity.Marketing_Vendor__c","Opportunity.Processor__r.Name","Opportunity.Processor__c"],"optionalFields":["Opportunity.StageName","Opportunity.ForecastCategoryName","Opportunity.Probability"],"pageSize":200,"sortBy":["-Opportunity.CreatedDate"]}}}]
    }),
    'aura.context': JSON.stringify({
        mode: "PROD",
        fwuid: fwuid,
        app: "one:one",
        loaded: {
            "APPLICATION@markup://one:one": "3741_e8jTwyKShfsfFm38joU73w"
        },
        dn: [],
        globals: {
            density: "VIEW_TWO",
            appContextId: "00000000000000000000"
        },
        uad: true
    }),
    'aura.pageURI': '/lightning/o/Opportunity/list?filterName=Default_Opportunity_Pipeline',
    'aura.token': token
});

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function fetchRecordDetails(recordId) {
    const secondPayload = new URLSearchParams({
        message: JSON.stringify({
            actions: [
                {
                    id: "18716;a",
                    descriptor: "aura://RecordUiController/ACTION$getRecordWithFields",
                    callingDescriptor: "UNKNOWN",
                    params: {
                        recordId: recordId,
                        optionalFields: [
                            "Opportunity.Name",
                            "Opportunity.Applicant_Mobile_Phone__c",
                            "Opportunity.Approx_Debt__c",
                            "Opportunity.Applicant_State_Code__c",
                            "Opportunity.CreatedBy.Name",
                            "Opportunity.CreatedDate"
                        ]
                    }
                }
            ]
        }),
        'aura.context': JSON.stringify({
            mode: "PROD",
            fwuid: fwuid,
            app: "one:one",
            loaded: {
                "APPLICATION@markup://one:one": "3741_e8jTwyKShfsfFm38joU73w"
            },
            dn: [],
            globals: {
                density: "VIEW_TWO",
                appContextId: "00000000000000000000"
            },
            uad: true
        }),
        'aura.pageURI': '/lightning/o/Opportunity/list?filterName=Default_Opportunity_Pipeline',
        'aura.token': token
    });

    const response = await fetch("https://clearoneadvantage.lightning.force.com/aura?r=1&aura.token=" + token, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        },
        body: secondPayload,
        credentials: 'include'
    });

    const data = await response.json();
    const fields = data.actions[0].returnValue.fields;

    return fields.Applicant_Mobile_Phone__c?.value || "No disponible";
}

function exportToCSV(data) {
    if (!data.length) {
        console.warn("No hay datos para exportar.");
        return;
    }

    const keys = Object.keys(data[0]);
    const csvRows = [];

    // Header
    csvRows.push(keys.join(','));

    // Rows
    data.forEach(row => {
        const values = keys.map(k => {
            const val = row[k] ?? '';
            return `"${String(val).replace(/"/g, '""')}"`;
        });
        csvRows.push(values.join(','));
    });

    const csvString = csvRows.join('\n');
    const blob = new Blob([csvString], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'datos_exportados.csv';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    console.log("✅ Datos exportados a datos_exportados.csv");
}

async function processAllRecords() {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: body,
            credentials: 'include'
        });

        const data = await response.json();
        const records = data.actions[0].returnValue.records;

        console.log(`Total registros: ${records.length}`);

        const AllCustomers = []

        // Formatear dateSearchPhone para comparación (MM/DD/YYYY)
        const targetDate = new Date(dateSearchPhone);
        // Solo queremos la fecha sin hora para comparar
        const targetDateString = targetDate.toLocaleDateString('en-US');

        for (let i = 0; i < records.length; i++) {
            const record = records[i];
            const recordId = record.fields.Id.value;
            const name = record.fields.Name.value;
            const owner = record.fields.Owner.value.fields.Name.value;

            const fullDate = record.fields.CreatedDate.displayValue; // ej: "6/5/2025, 5:26 PM"
            const onlyDate = fullDate.split(',')[0].trim(); // "6/5/2025"


            const recordDate = new Date(onlyDate);
            const recordDateString = recordDate.toLocaleDateString('en-US');

            console.log(recordDateString)
            if (recordDateString === targetDateString) {


                const telefono = await fetchRecordDetails(recordId);
console.log("Telefono: ", telefono)
                AllCustomers.push({
                    CustomerId: recordId,
                    CustomerName: name,
                    Owner: owner,
                    CustomerPhone: telefono
                });


                if (AllCustomers.length % 5 === 0) {
                    exportToCSV(AllCustomers);
                    AllCustomers.length = 0; // limpiar array para siguiente bloque
                    console.log(`📤 Exportados ${i + 1} registros filtrados.`);
                }


                if (i < records.length - 1) {
                    await delay(1000);
                }
            } else {

                console.log(`🗓 Ignorado registro (${i + 1}) por fecha: ${onlyDate}`);
            }
            console.log(AllCustomers)
        }


        if (AllCustomers.length > 0) {
            exportToCSV(AllCustomers);
            console.log(`📤 Exportados los últimos ${AllCustomers.length} registros filtrados.`);
        }

    } catch (error) {
        console.error("❌ Error:", error);
    }
}


processAllRecords();



