import sys

def summarize(diff_file):
    with open(diff_file, "r") as f:
        diff = f.read()

    # Contar líneas agregadas y eliminadas
    added = sum(1 for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++"))
    removed = sum(1 for line in diff.splitlines() if line.startswith("-") and not line.startswith("---"))

    print(f"""
<!-- AI SUMMARY START -->

## 🧾 AI Summary

### 📊 Cambios detectados
- Líneas agregadas: {added}
- Líneas eliminadas: {removed}

### 🧪 Impacto QA
- Revisar cobertura de tests
- Validar casos borde
- Verificar ausencia de debug prints

### ⚠️ Riesgo estimado
- Bajo / Medio (requiere validación manual)

---
_Generado automáticamente_

<!-- AI SUMMARY END -->
""")

if __name__ == "__main__":
    summarize(sys.argv[1])
