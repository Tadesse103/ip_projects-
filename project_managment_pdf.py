from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Title
pdf.set_font("Arial", size=16, style='B')
pdf.cell(200, 10, txt="Detailed Project Management for Building Construction (Start to Finish)", ln=True, align='C')

# Line break
pdf.ln(10)

# Content Sections
content = [
    ("1. Project Initiation", """
Objective:
- Define the project scope, objectives, and feasibility.
- Secure project funding and stakeholder approvals.

Key Tasks:
- Conduct a site analysis and feasibility study.
- Obtain necessary permits and legal approvals.
- Form the project team, including the project manager, architects, engineers, and contractors.

Deliverables:
- Project Charter.
- Feasibility Report.
- Stakeholder Agreement.
    """),

    ("2. Project Planning", """
Objective:
- Plan all aspects of the project, including design, budgeting, scheduling, and resource management.

Key Tasks:
- Develop a detailed project schedule using project management software (e.g., Gantt charts).
- Create a project budget and allocate resources.
- Define the project scope, objectives, and deliverables.
- Select contractors and suppliers.
- Design the building structure, architecture, and systems (plumbing, electrical, HVAC).
- Establish risk management strategies.

Deliverables:
- Project Plan (including scope, timeline, budget, risk management).
- Detailed Design Drawings.
- Procurement Plan.
- Risk Management Plan.
    """),

    ("3. Design Phase", """
Objective:
- Finalize architectural designs, structural plans, and other technical drawings.
- Obtain all necessary permits before construction begins.

Key Tasks:
- Finalize architectural designs, including layout, aesthetics, and space planning.
- Structural engineering and mechanical system design (HVAC, electrical, plumbing).
- Coordinate with environmental consultants for sustainability.
- Submit designs to local authorities for approval.

Deliverables:
- Approved Architectural and Structural Designs.
- Approved Permits for Construction.
- Sustainability and Environmental Impact Report.
    """),

    ("4. Pre-Construction Phase", """
Objective:
- Prepare for construction by procuring materials and hiring contractors.
- Set up the construction site.

Key Tasks:
- Hire contractors, subcontractors, and construction workers.
- Procure necessary materials and equipment.
- Set up temporary facilities (offices, storage, etc.) on-site.
- Perform site preparation (surveying, grading, fencing, utilities).
- Develop safety protocols and training for workers.

Deliverables:
- Contractor and Subcontractor Agreements.
- Procurement Records.
- Site Preparation Report.
- Safety Plan.
    """),

    ("5. Construction Phase", """
Objective:
- Begin actual construction of the building, following all plans and schedules.

Key Tasks:
- Clear the site and prepare the foundation.
- Build the structural framework (steel, concrete, etc.).
- Install plumbing, electrical, and HVAC systems.
- Construct the exterior (walls, windows, roofing).
- Build the interior spaces (flooring, walls, doors).
- Monitor project progress and quality at every stage.

Deliverables:
- Progress Reports (Weekly or Bi-weekly).
- Completed Foundation, Structure, and Core Services.
- Building Systems Installation (Plumbing, Electrical, HVAC).
    """),

    ("6. Interior and Exterior Finishes", """
Objective:
- Complete the detailed work that will give the building its final appearance and functionality.

Key Tasks:
- Install interior finishes (paint, flooring, ceilings, and fixtures).
- Complete exterior work (landscaping, pavement, signage).
- Conduct inspections for quality assurance.
- Install furniture and fittings as required.

Deliverables:
- Completed Interior and Exterior Finishes.
- Final Inspection Reports.
- Furniture and Fixtures Installation.
    """),

    ("7. Quality Control and Inspections", """
Objective:
- Ensure all work complies with regulatory standards and the project’s requirements.

Key Tasks:
- Conduct regular quality assurance inspections.
- Inspect materials and workmanship for compliance.
- Address any issues or rework necessary.
- Conduct safety inspections and ensure compliance with OSHA standards.
- Perform final checks for building code compliance.

Deliverables:
- Quality Inspection Reports.
- Safety Compliance Certificates.
- Corrective Action Reports (if any).
    """),

    ("8. Project Handover", """
Objective:
- Deliver the finished building to the client or stakeholders.

Key Tasks:
- Conduct a final walk-through with stakeholders to ensure satisfaction.
- Handover all documentation (warranties, operation manuals, as-built drawings).
- Finalize any remaining financial transactions.
- Decommission temporary site offices and storage.

Deliverables:
- Project Handover Document (includes all records, manuals, and warranties).
- Final Payment to Contractors.
- Project Completion Report.
    """),

    ("9. Post-Construction Support and Maintenance", """
Objective:
- Provide ongoing support for the building, including maintenance and addressing any issues that arise post-completion.

Key Tasks:
- Set up a maintenance schedule for HVAC, plumbing, electrical systems, etc.
- Address any warranty issues or defects that appear.
- Conduct post-occupancy evaluations for user feedback and operational improvements.

Deliverables:
- Maintenance Schedule.
- Warranty Documentation.
- Post-Occupancy Evaluation Report.
    """),

    ("10. Project Closure and Review", """
Objective:
- Close out the project by evaluating its success, documenting lessons learned, and releasing resources.

Key Tasks:
- Conduct a final project review with the team and stakeholders.
- Document any lessons learned during the project.
- Release project resources and prepare a final financial report.
- Archive project documentation for future reference.

Deliverables:
- Final Project Review Document.
- Lessons Learned Report.
- Project Closeout Report.
    """)
]

# Set font for the content
pdf.set_font("Arial", size=12)

# Add content to the PDF
for section_title, section_content in content:
    pdf.cell(200, 10, txt=section_title, ln=True, align='L')
    pdf.multi_cell(0, 10, section_content)
    pdf.ln(5)

# Save the PDF to a file
file_path = "Building_Construction_Project_Management_Detailed.pdf"
pdf.output(file_path)

print(f"PDF saved to {file_path}")

