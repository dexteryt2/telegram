import re,sys,pathlib
root=pathlib.Path(sys.argv[1]); api_id,api_hash=(sys.argv[2:4]+["",""])[:2]
A=0.10  # pill/panel layer opacity (stock 0.85 / 0.76)
f=root/"TMessagesProj/src/main/java/org/telegram/ui/Components/blur3/drawable/color/impl/BlurredBackgroundProviderImpl.java"
s=f.read_text(); n=s.count("? 0.85f : 0.76f")
s=s.replace("? 0.85f : 0.76f",f"? {A}f : {A}f"); f.write_text(s)
g=root/"TMessagesProj/src/main/java/org/telegram/ui/Components/blur3/drawable/color/BlurredBackgroundColorProviderThemed.java"
t=g.read_text(); t=t.replace("? 0.85f : 0.76f",f"? {A}f : {A}f"); g.write_text(t)
if api_id and api_hash:
  b=root/"TMessagesProj/src/main/java/org/telegram/messenger/BuildVars.java"
  v=b.read_text()
  v=re.sub(r"APP_ID\s*=\s*\d+;",f"APP_ID = {api_id};",v); v=re.sub(r'APP_HASH\s*=\s*"[^"]*";',f'APP_HASH = "{api_hash}";',v)
  b.write_text(v)
print("patched alpha sites:",n)
