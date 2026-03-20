import sys
import re
import json


def analyze_diff(diff_text):
    lines = diff_text.split("\n")

    current_file = None
    current_line = 0

    comments = []
    seen = set()  # 🔥 evita duplicados por archivo + tipo

    for line in lines:

        if line.startswith("diff --git"):
            match = re.search(r"b/(.+)", line)
            if match:
                current_file = match.group(1)

        elif line.startswith("@@"):
            match = re.search(r"\+(\d+)", line)
            if match:
                current_line = int(match.group(1))

        elif line.startswith("+") and not line.startswith("+++"):
            content = line[1:]

            # 📝 TODO detection
            if "TODO" in content:
                if "(" not in content:
                    severity = "medium"
                    body = "TODO sin contexto — debería detallarse o resolverse antes del merge"
                    icon = "🟡"
                    score = 3
                else:
                    severity = "low"
                    body = "TODO pendiente"
                    icon = "🟢"
                    score = 1

                key = (current_file, "TODO")
                if key not in seen:
                    comments.append({
                        "path": current_file,
                        "line": current_line,
                        "body": body,
                        "severity": severity,
                        "score": score,
                        "icon": icon
                    })
                    seen.add(key)

            # 🧪 print detection
            if "print(" in content:
                key = (current_file, "print")

                if key not in seen:
                    comments.append({
                        "path": current_file,
                        "line": current_line,
                        "body": "Debug print detectado — usar logging en lugar de print",
                        "severity": "low",
                        "score": 1,
                        "icon": "🟢"
                    })
                    seen.add(key)

            current_line += 1

        else:
            if not line.startswith("-"):
                current_line += 1

    return comments


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        diff = f.read()

    comments = analyze_diff(diff)

    print(json.dumps(comments))
