"""Build a portable HTML reader from already aligned bilingual JSON. No dependencies."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def build(data,output):
    assert isinstance(data['id'],str) and isinstance(data['title'],str)
    assert data['pairs'] and all(isinstance(p['en'],str) and isinstance(p['zh'],str) for p in data['pairs'])
    page=(ROOT/'template.html').read_text()
    for key,value in [('STYLE',(ROOT/'style.css').read_text()),('SCRIPT',(ROOT/'app.js').read_text()),('DATA',json.dumps(data,ensure_ascii=False).replace('<','\\u003c'))]:
        page=page.replace('{{'+key+'}}',value,1)
    Path(output).write_text(page)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('input',nargs='?',default=str(ROOT/'example.json'));parser.add_argument('-o','--output',default=str(ROOT/'index.html'));args=parser.parse_args()
    build(json.loads(Path(args.input).read_text()),args.output)
