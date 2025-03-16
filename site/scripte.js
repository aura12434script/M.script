function runCode() {
    const code = document.getElementById("code").value;
    const consoleOutput = document.getElementById("console");
    consoleOutput.textContent = ""; // مسح وحدة التحكم قبل التشغيل
  
    // دالة وهمية للتنفيذ (استبدلها بالكود الفعلي الخاص بك)
    try {
      const result = executeMscript(code);
      consoleOutput.textContent = result; // عرض النتيجة
    } catch (error) {
      consoleOutput.textContent = "Error: " + error.message; // عرض الخطأ
    }
  }
  
  function executeMscript(code) {
    // هنا ضع كود التنفيذ الخاص بك (المفسر)
    return "Executing: " + code; // مثال بسيط
  }
  
  function updateLineNumbers() {
    const codeEditor = document.getElementById("code");
    const lineNumbers = document.getElementById("line-numbers");
    const lines = codeEditor.value.split('\n');
    let numbers = '';
    for (let i = 1; i <= lines.length; i++) {
      numbers += i + '<br>';
    }
    lineNumbers.innerHTML = numbers;
  }
  
  // تحديث أرقام الأسطر عند تحميل الصفحة
  window.onload = updateLineNumbers;