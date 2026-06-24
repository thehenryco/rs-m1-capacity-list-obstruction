from pathlib import Path
import json
import textwrap
from datetime import datetime, timezone

pkg = Path("runs/PRE_SUBMISSION_M1_SPECIALIZATION_PACKAGE")
pub = Path("public/rs-m1-capacity-list-obstruction")
repo_url = "https://github.com/thehenryco/rs-m1-capacity-list-obstruction"
status_label = "Public pre-submission draft. GitHub timestamp posted. m=1 notation alignment, final conflict disclosure, and prior-work positioning included. Not yet an official Proximity Prize submission pending academic repository posting and peer-review acceptance."

prior = []
prior.append("## Prior-Work Positioning")
prior.append("")
prior.append("The Proximity Prize targets Reed-Solomon list-decoding and correlated-agreement challenges formalized in the companion paper Open Problems in List Decoding and Correlated Agreement by Arnon, Boneh, and Fenzi. This draft is positioned as an m=1 ordinary-list specialization, not as a claim about the full mutual correlated agreement object or arbitrary constant m.")
prior.append("")
prior.append("Classical Reed-Solomon list decoding studies the size of Hamming balls around received words and the radius at which many codewords can appear. The construction in this draft is elementary but directly exposes the capacity-radius surface: for C = RS[F_q,L,k], a received word y with no degree < k polynomial agreeing on more than k coordinates has exactly binom(n,k) codewords at radius n-k.")
prior.append("")
prior.append("Johnson-type bounds and capacity-style results are usually used to upper-bound list size below or near decoding thresholds. This note instead gives a lower-bound obstruction at the capacity-radius boundary delta = 1-k/n. It should therefore be read as a specialization/edge-case obstruction that must be compared carefully against the exact Lambda(C^{equiv m},delta) definitions in the Proximity Prize companion paper.")
prior.append("")
prior.append("Recent work around Reed-Solomon proximity gaps relates proximity-gap behavior to list-decodability limits. This draft does not claim to improve those results. It isolates the m=1 ordinary-list object and supplies a transparent construction showing threshold failure in the field-size window binom(n,k+1) < q < 2^128 binom(n,k).")

notation = []
notation.append("## Companion-Paper Notation Alignment")
notation.append("")
notation.append("This draft aligns to the m=1 specialization of the grand list-decoding notation. In that specialization, C^{equiv 1} is treated as the ordinary Reed-Solomon code C, and Lambda(C^{equiv 1},delta) is treated as the ordinary list of codewords within relative Hamming radius delta of a received word y.")
notation.append("")
notation.append("The theorem proves that at delta = 1-k/n, there exists y such that |Lambda(C^{equiv 1},y,delta)| = binom(n,k). When binom(n,k+1) < q < 2^128 binom(n,k), this exceeds 2^-128 |F_q|.")
notation.append("")
notation.append("This notation alignment does not assert the arbitrary constant-m case. The arbitrary-m object remains outside this draft unless a separate m-wise construction is added.")

conflict = []
conflict.append("## Final Conflict Disclosure")
conflict.append("")
conflict.append("The author declares no known financial, institutional, employment, advisory, or personal conflicts of interest that would affect this pre-submission draft. The public GitHub repository is owned by the author through the thehenryco GitHub account.")

paper_path = pkg / "paper.md"
paper = paper_path.read_text(encoding="utf-8")
paper = paper.replace("Status: PRE-SUBMISSION DRAFT", "Status: " + status_label)
paper = paper.replace("Status: PRE-SUBMISSION / EARLY-RESULT INQUIRY DRAFT", "Status: " + status_label)
paper = paper.replace("Repository link: TO_BE_ADDED_AFTER_PUBLIC_POSTING", "GitHub timestamp repository: " + repo_url + "\\nAcademic repository link: TO_BE_ADDED_AFTER_ARXIV_OR_IACR_POSTING")
paper = paper.replace("Peer-review status: TO_BE_ADDED_AFTER_CONFERENCE_OR_JOURNAL_ACCEPTANCE", "Peer-review status: TO_BE_ADDED_AFTER_CONFERENCE_OR_JOURNAL_ACCEPTANCE")
paper = paper.replace("TO_BE_EXPANDED. The final version should compare this result with the Proximity Prize companion paper, classical Reed-Solomon list decoding, Johnson-type bounds, capacity-radius behavior, and known impossibility or near-capacity results. This section must identify whether the m=1 specialization is explicitly covered by the prize definitions or whether it is submitted as a specialization/partial result.", "\\n".join(prior).replace("## Prior-Work Positioning\\n\\n", ""))

if "## Prior-Work Positioning" not in paper:
    paper += "\\n" + "\\n".join(prior) + "\\n"
if "## Companion-Paper Notation Alignment" not in paper:
    paper += "\\n" + "\\n".join(notation) + "\\n"
if "## Final Conflict Disclosure" not in paper:
    paper += "\\n" + "\\n".join(conflict) + "\\n"
if "## Academic Repository Metadata" not in paper:
    paper += "\\n## Academic Repository Metadata\\n\\nAcademic repository status: TO_BE_ADDED_AFTER_ARXIV_OR_IACR_POSTING\\n\\nSuggested arXiv categories: cs.IT, math.IT, cs.CR\\n\\nSuggested IACR area: cryptology / coding-theory-adjacent foundations for proximity testing and list decoding.\\n"

paper_path.write_text(paper, encoding="utf-8")

cover = []
cover.append("# Cover Note - Public Pre-Submission Draft")
cover.append("")
cover.append("To: proximityprize@ethereum.org")
cover.append("Subject: Public pre-submission draft - m=1 Reed-Solomon capacity-radius list obstruction")
cover.append("")
cover.append("Dear Proximity Prize Committee,")
cover.append("")
cover.append("I am preparing a possible submission related to the Reed-Solomon grand list-decoding challenge and would like to clarify whether the attached m=1 specialization is within scope as a partial result.")
cover.append("")
cover.append("GitHub timestamp repository: " + repo_url)
cover.append("Academic repository link: TO_BE_ADDED_AFTER_ARXIV_OR_IACR_POSTING")
cover.append("Peer-review status: TO_BE_ADDED_AFTER_ACCEPTANCE")
cover.append("")
cover.append("The draft proves that, for C = RS[F_q,L,k], if binom(n,k+1) < q < 2^128 binom(n,k), then there exists y such that |Lambda(C,y,n-k)| = binom(n,k) > 2^-128 |F_q| at delta = 1-k/n.")
cover.append("")
cover.append("This is not represented as a final official prize submission yet. Remaining official-submission steps are academic repository posting and peer-review acceptance.")
cover.append("")
cover.append("Final conflict disclosure: I declare no known financial, institutional, employment, advisory, or personal conflicts of interest that would affect this pre-submission draft. The public GitHub repository is owned by me through the thehenryco GitHub account.")
cover.append("")
cover.append("Sincerely,")
cover.append("Jerod Harbor")
(pkg / "cover_note.md").write_text("\\n".join(cover), encoding="utf-8")

arxiv = []
arxiv.append("# arXiv Metadata Draft")
arxiv.append("")
arxiv.append("Title: A Capacity-Radius List-Decoding Obstruction for the m=1 Specialization of Reed-Solomon Codes")
arxiv.append("Author: Jerod Harbor")
arxiv.append("Categories: cs.IT; math.IT; cs.CR")
arxiv.append("Repository: " + repo_url)
arxiv.append("Status: TO_BE_SUBMITTED_BY_AUTHOR")
arxiv.append("")
arxiv.append("Abstract: We give a capacity-radius list-decoding obstruction for the m=1 specialization of Reed-Solomon codes. Let C = RS[F_q,L,k] with |L|=n. We prove that, whenever q > binom(n,k+1), there exists a received word y for which the Hamming ball of radius n-k contains exactly binom(n,k) Reed-Solomon codewords. Consequently, if binom(n,k+1) < q < 2^128 binom(n,k), then |Lambda(C,y,n-k)| = binom(n,k) > 2^-128 |F_q|.")
(pkg / "ARXIV_METADATA_DRAFT.md").write_text("\\n".join(arxiv), encoding="utf-8")

iacr = []
iacr.append("# IACR ePrint Metadata Draft")
iacr.append("")
iacr.append("Title: A Capacity-Radius List-Decoding Obstruction for the m=1 Specialization of Reed-Solomon Codes")
iacr.append("Author: Jerod Harbor")
iacr.append("Repository: " + repo_url)
iacr.append("Status: TO_BE_SUBMITTED_BY_AUTHOR")
iacr.append("")
iacr.append("Abstract: This note gives an m=1 ordinary-list specialization for Reed-Solomon capacity-radius list size. It proves exact list size binom(n,k) at radius n-k under a generic received-word condition and derives threshold failure for binom(n,k+1) < q < 2^128 binom(n,k).")
(pkg / "IACR_EPRINT_METADATA_DRAFT.md").write_text("\\n".join(iacr), encoding="utf-8")

check = []
check.append("# Pre-Submission Checklist")
check.append("")
check.append("- [x] theorem statement")
check.append("- [x] proof")
check.append("- [x] m=1 specialization scope")
check.append("- [x] final conflict disclosure")
check.append("- [x] PDF compiled")
check.append("- [x] GitHub timestamp posted")
check.append("- [x] GitHub URL inserted into package")
check.append("- [x] expanded prior-work positioning")
check.append("- [x] m=1 companion-paper notation alignment")
check.append("- [x] arXiv metadata draft")
check.append("- [x] IACR ePrint metadata draft")
check.append("- [ ] arXiv or IACR ePrint academic repository posting")
check.append("- [ ] peer-review acceptance added")
check.append("- [ ] official submission cover note finalized after acceptance")
(pkg / "pre_submission_checklist.md").write_text("\\n".join(check), encoding="utf-8")

manifest_path = pkg / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["status"] = "PUBLIC_PRE_SUBMISSION_DRAFT_GITHUB_TIMESTAMP_POSTED_LOCAL_ITEMS_COMPLETED"
manifest["status_label"] = status_label
manifest["public_repository_url"] = repo_url
manifest["public_repository_status"] = "POSTED"
manifest["academic_repository_url"] = "TO_BE_ADDED_AFTER_ARXIV_OR_IACR_POSTING"
manifest["academic_repository_status"] = "NOT_POSTED"
manifest["prior_work_positioning"] = "INCLUDED_DRAFT"
manifest["final_conflict_disclosure"] = "INCLUDED"
manifest["notation_alignment"] = "M_EQUALS_1_SPECIALIZATION_INCLUDED"
manifest["arxiv_metadata_draft"] = "ARXIV_METADATA_DRAFT.md"
manifest["iacr_metadata_draft"] = "IACR_EPRINT_METADATA_DRAFT.md"
manifest["official_submission_ready"] = False
manifest["missing_before_official_submission"] = ["academic repository posting", "peer-review acceptance"]
manifest["updated_utc"] = datetime.now(timezone.utc).isoformat()
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

status = []
status.append("# SUBMISSION STATUS")
status.append("")
status.append("Updated UTC: " + datetime.now(timezone.utc).isoformat())
status.append("")
status.append("## Status Label")
status.append(status_label)
status.append("")
status.append("## Build State")
status.append("- PDF_READY: yes")
status.append("- GITHUB_TIMESTAMP_READY: yes")
status.append("- GITHUB_URL: " + repo_url)
status.append("- PRIOR_WORK_READY: yes")
status.append("- CONFLICT_DISCLOSURE_READY: yes")
status.append("- PRIZE_NOTATION_ALIGNMENT_READY: yes for m=1 specialization")
status.append("- ARXIV_METADATA_READY: yes")
status.append("- IACR_METADATA_READY: yes")
status.append("- ACADEMIC_REPOSITORY_READY: not yet")
status.append("- PEER_REVIEW_READY: not yet")
status.append("- OFFICIAL_SUBMISSION_READY: not yet")
status.append("")
status.append("## Missing Before Official Submission")
status.append("- academic repository posting")
status.append("- peer-review acceptance")
(pkg / "README_SUBMISSION_STATUS.md").write_text("\\n".join(status), encoding="utf-8")

def normalize(s):
    return s.encode("ascii", "replace").decode("ascii")
def pdf_escape(s):
    return s.replace("\\\\", "\\\\\\\\").replace("(", "\\\\(").replace(")", "\\\\)")
text = (pkg / "paper.md").read_text(encoding="utf-8")
items = []
for raw in text.splitlines():
    line = normalize(raw.rstrip())
    if line.startswith("# "):
        for part in textwrap.wrap(line[2:], width=54): items.append(("TITLE", part))
    elif line.startswith("## "):
        for part in textwrap.wrap(line[3:], width=70): items.append(("H1", part))
    elif line.startswith("### "):
        for part in textwrap.wrap(line[4:], width=78): items.append(("H2", part))
    elif line.startswith("- "):
        for part in textwrap.wrap(line[2:], width=88): items.append(("BODY", "- " + part))
    elif line.strip() == "": items.append(("BLANK", ""))
    else:
        for part in textwrap.wrap(line, width=92): items.append(("BODY", part))
pages=[]; current=[]; y=742
for kind,line in items:
    step = 10 if kind=="BLANK" else 15
    if kind=="TITLE": step=24
    if kind=="H1": step=22
    if kind=="H2": step=18
    if y-step < 60: pages.append(current); current=[]; y=742
    current.append((kind,line,y)); y -= step
if current: pages.append(current)
objects=[]
def add(body): objects.append(body); return len(objects)
f1=add("<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman >>")
f2=add("<< /Type /Font /Subtype /Type1 /BaseFont /Times-Bold >>")
content_ids=[]
for page in pages:
    sl=["BT"]
    for kind,line,yy in page:
        if kind=="BLANK": continue
        font="/F1 10 Tf"
        if kind=="TITLE": font="/F2 15 Tf"
        elif kind=="H1": font="/F2 13 Tf"
        elif kind=="H2": font="/F2 11 Tf"
        sl.append(font); sl.append("72 "+str(yy)+" Td ("+pdf_escape(line)+") Tj"); sl.append("-72 -"+str(yy)+" Td")
    sl.append("ET")
    stream="\\n".join(sl)
    content_ids.append(add("<< /Length "+str(len(stream.encode("ascii")))+" >>\\nstream\\n"+stream+"\\nendstream"))
pages_obj_id=2+len(content_ids)+len(pages)+1
page_ids=[]
for cid in content_ids: page_ids.append(add("<< /Type /Page /Parent "+str(pages_obj_id)+" 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 "+str(f1)+" 0 R /F2 "+str(f2)+" 0 R >> >> /Contents "+str(cid)+" 0 R >>"))
kids=" ".join(str(pid)+" 0 R" for pid in page_ids)
pages_id=add("<< /Type /Pages /Kids ["+kids+"] /Count "+str(len(page_ids))+" >>")
catalog_id=add("<< /Type /Catalog /Pages "+str(pages_id)+" 0 R >>")
pdf=bytearray(); pdf.extend(b"%PDF-1.4\\n"); offsets=[0]
for i,obj in enumerate(objects,start=1): offsets.append(len(pdf)); pdf.extend((str(i)+" 0 obj\\n").encode("ascii")); pdf.extend(obj.encode("ascii")); pdf.extend(b"\\nendobj\\n")
xref=len(pdf); pdf.extend(("xref\\n0 "+str(len(objects)+1)+"\\n").encode("ascii")); pdf.extend(b"0000000000 65535 f \\n")
for off in offsets[1:]: pdf.extend(("{:010d} 00000 n \\n".format(off)).encode("ascii"))
pdf.extend(("trailer\\n<< /Size "+str(len(objects)+1)+" /Root "+str(catalog_id)+" 0 R >>\\nstartxref\\n"+str(xref)+"\\n%%EOF\\n").encode("ascii"))
(pkg / "paper.pdf").write_bytes(pdf)

pub.mkdir(parents=True, exist_ok=True)
copies = {"paper.pdf":"paper.pdf","paper.md":"README.md","paper.tex":"paper.tex","cover_note.md":"cover_note.md","manifest.json":"manifest.json","README_SUBMISSION_STATUS.md":"README_SUBMISSION_STATUS.md","pre_submission_checklist.md":"pre_submission_checklist.md","ARXIV_METADATA_DRAFT.md":"ARXIV_METADATA_DRAFT.md","IACR_EPRINT_METADATA_DRAFT.md":"IACR_EPRINT_METADATA_DRAFT.md"}
for s,d in copies.items(): (pub / d).write_bytes((pkg / s).read_bytes())

print("LOCAL_FINISHABLE_ITEMS_COMPLETED")
print("remaining: academic repository posting, peer-review acceptance")
print("package:", pkg.resolve())
print("public:", pub.resolve())
