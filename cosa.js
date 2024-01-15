// let query = window.location.href.replace(window.origin, "1|");
//  query = window.location.href.replace(window.location.pathname, "1|");

//  if(query.includes("?")){
//     query = "?p=t";
//  }else{
//     query = "&p=t";
//  }

// //  var Results = [
// //    ["Col1", "Col2", "Col3", "Col4"],
// //    ["Data", 50, 100, 500],
// //    ["Data", -100, 20, 100],
// //  ];
// //  const columns =["Col1", "Col2", "Col3", "Col4"];
// // const data =[
// //    ["Data", 50, 100, 500],
// //    ["Data", -100, 20, 100],
// // ];
// //    var CsvString = "";
// //    /*

// //    Results.forEach(function (RowItem, RowIndex) {
// //      RowItem.forEach(function (ColItem, ColIndex) {
// //        CsvString += ColItem + ",";
// //      });
// //      CsvString += "\r\n";
// //    });

// // */

// //    for (let i = 0; i < array.length; i++) {
// //       const element = array[i];

// //    }

// const input = $('#fileInput')

// input.addEventListener('change', async (e) => {
//   const file = e.target.files[0]

//   if (!file) return

//   const data = await file.arrayBuffer()

//   const wb = XLSX.read(data)
//   const ws = wb.Sheets[wb.SheetNames[0]]
//   const result = XLSX.utils.sheet_to_json(ws, {
//     header: 1
//   })

//   $('#result').innerHTML = JSON.stringify(result, null, 2)
// })

// var Results = [
//    ["Col1", "Col2", "Col3", "Col4"],
//    ["Data", 50, 100, 500],
//    ["Data", -100, 20, 100],
//  ];

//  async function Table2XLSX() {
//    /* Callback invoked when the button is clicked */

//  }

const data = [

    { id: 1, name: "asd", age: 1 },
    { id: 2, name: "pfx7r4ef91", age: 43 },
    { id: 3, name: "ab07pqmbc8", age: 78 },
    { id: 4, name: "mri7zb9pzn", age: 23 },
    { id: 5, name: "b0bvs6jc4k", age: 65 },
    { id: 6, name: "snad892r7g", age: 73 },
    { id: 7, name: "h4jxm38c97", age: 76 },
    { id: 8, name: "xu0wr1o8zq", age: 32 },
    { id: 9, name: "w7fi8l57r6", age: 94 },
    { id: 10, name: "rqilw7s12p", age: 17 },

];

const prepare_data_to_xls =(base,data)=>{
   const data_xls = [];
   
   data_xls.push(base.map(b => b.verbose))

   data.map(d =>{
      const element = [];
      base.map(b =>{
         element.push(d[b.key])
      })
      data_xls.push(element)
   })


   return data_xls
}

const create_XLS = async (base,data) => {
  const XLSX = await import(
    "https://cdn.sheetjs.com/xlsx-0.20.1/package/xlsx.mjs"
  );

  const wb = XLSX.utils.book_new();
  const ws = XLSX.utils.aoa_to_sheet(prepare_data_to_xls(base,data));
  XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
  XLSX.writeFile(wb, "SheetJSESMTest.xlsx");
};


// create_XLS([{verbose : "Nombre", key : "name"},{verbose : "Edad", key : "age"}],data);


// const get_date =()=>{
//    let date = "";
//    const rawdate = new Date();
//    date = `[${rawdate.getDay()}/${rawdate.getMonth()}/${rawdate.getFullYear()}]`


//    console.log(rawdate);
// }


// get_date()




if (actual_page + (max_btns - 1) >= max) {
   let cicle = 0;
   for (let i = max_btns; i > 0; i--) {
     const btn = $("<a/>");
     btn.attr({
       class: `paginate_button ${
         actual_page - (i - 1) == actual_page ? "current" : ""
       }`,
     });
     btn.text(actual_page - (i - 1));
     container.append(btn);
   }
 } else {
   for (let i = 0; i < max_btns; i++) {
     if (actual_page + i <= max) {
       const btn = $("<a/>");
       btn.attr({
         class: `paginate_button ${
           actual_page == actual_page + i ? "current" : ""
         }`,
       });
       btn.text(actual_page + i);
       container.append(btn);
     }
   }
 }



 for (let index = 0; index < array.length; index++) {
   const element = array[index];
   
 }
