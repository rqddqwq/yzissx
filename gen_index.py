import os, json

folder = "./content"
names = []
for fn in os.listdir(folder):
    if fn.endswith(".md"):
        names.append(fn[:-3])

out_path = os.path.join(folder, "index.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(names, f, ensure_ascii=False, indent=2)

print(f"已生成 {out_path}，共 {len(names)} 个md文档")
