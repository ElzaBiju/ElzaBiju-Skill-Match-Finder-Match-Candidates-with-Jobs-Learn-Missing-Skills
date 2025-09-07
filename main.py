file=open("Skillmatch.txt","w")
file1=open("cmp_match.txt","w")

candidates = {
    "Alice": {"Python", "Machine Learning", "Statistics", "SQL", "Pandas","Data Visualization","NumPy"},
    "Bob": {"HTML", "CSS", "JavaScript", "React", "Node.js", "Git"},
    "Charlie": {"Python", "Deep Learning", "TensorFlow", "PyTorch","NLP"},
    "Diana": {"SQL", "Database Design", "Backup","Performance Tuning", "Security"}}

jobs = {
    "Data Scientist": {"Python", "Machine Learning", "Statistics", "SQL", "Data Visualization", "Pandas", "NumPy"},
    "Web Developer": {"HTML", "CSS", "JavaScript", "React", "Node.js", "Git"},
    "AI Engineer": {"Python", "Deep Learning", "TensorFlow", "PyTorch", "NLP"},
    "Database Administrator": {"SQL", "Database Design", "Backup", "Performance Tuning", "Security"}}

path_dict = {
    "Python": "Python Tutorial (W3Schools) - https://www.w3schools.com/python/",
    "Java": "Java Programming (GeeksforGeeks) - https://www.geeksforgeeks.org/java/",
    "C++": "C++ Programming Guide (Programiz) - https://www.programiz.com/cpp-programming",
    "JavaScript": "JavaScript Basics (Mozilla MDN) - https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    "HTML": "HTML Basics (W3Schools) - https://www.w3schools.com/html/",
    "CSS": "CSS Tutorial (W3Schools) - https://www.w3schools.com/css/",
    "SQL": "SQL Tutorial (W3Schools) - https://www.w3schools.com/sql/",
    "R": "R Programming for Data Science (Datacamp) - https://www.datacamp.com/courses/free-introduction-to-r",
    "Kotlin": "Kotlin for Beginners (Kotlin Docs) - https://kotlinlang.org/docs/home.html",
    "Swift": "Swift Programming (Swift.org) - https://www.swift.org/",
    "C#": "C# Basics (Microsoft Learn) - https://learn.microsoft.com/en-us/dotnet/csharp/"
    ,"Machine Learning": "Intro to ML (Coursera - Andrew Ng) - https://www.coursera.org/learn/machine-learning",
    "Deep Learning": "Deep Learning Specialization (Coursera) - https://www.coursera.org/specializations/deep-learning",
    "TensorFlow": "TensorFlow Guide (Official) - https://www.tensorflow.org/learn",
    "PyTorch": "PyTorch Tutorials (Official) - https://pytorch.org/tutorials/",
    "NLP": "Natural Language Processing (Kaggle) - https://www.kaggle.com/learn/natural-language-processing",
    "Data Visualization": "Data Visualization with Python (Coursera) - https://www.coursera.org/learn/python-for-data-visualization",
    "Pandas": "Pandas Documentation - https://pandas.pydata.org/docs/",
    "NumPy": "NumPy Documentation - https://numpy.org/doc/",
    "Big Data": "Big Data Fundamentals (edX) - https://www.edx.org/course/big-data-fundamentals",
    "Spark": "Apache Spark (Databricks) - https://spark.apache.org/docs/latest/"
    ,"React": "React Official Docs - https://react.dev/",
    "Node.js": "Node.js Crash Course (YouTube) - https://www.youtube.com/watch?v=fBNz5xF-Kx4",
    "Full Stack": "Full-Stack Web Dev (freeCodeCamp) - https://www.freecodecamp.org/learn/",
    "Git": "Git Basics (freeCodeCamp) - https://www.freecodecamp.org/news/git-and-github-for-beginners/",
    "CI/CD": "CI/CD Basics (Atlassian) - https://www.atlassian.com/continuous-delivery/ci-vs-ci-vs-cd",
    "Docker": "Docker Handbook (GeeksforGeeks) - https://www.geeksforgeeks.org/docker-tutorial/",
    "Kubernetes": "Kubernetes Docs - https://kubernetes.io/docs/tutorials/"
    ,"AWS": "AWS Cloud Practitioner Essentials - https://aws.amazon.com/training/digital/",
    "Azure": "Microsoft Azure Fundamentals - https://learn.microsoft.com/en-us/certifications/azure-fundamentals/",
    "Linux": "Linux Basics (Linux Journey) - https://linuxjourney.com/",
    "Networking": "Computer Networking Basics (Khan Academy) - https://www.khanacademy.org/computing/computer-science/internet-intro",
    "Routing": "Cisco Networking Basics - https://skillsforall.com/course/networking-basics",
    "Switching": "Cisco Switching Concepts - https://skillsforall.com/",
    "Firewalls": "Firewall Fundamentals (Imperva Blog) - https://www.imperva.com/learn/application-security/firewall/",
    "Risk Assessment": "Risk Management Basics (Coursera) - https://www.coursera.org/learn/enterprise-risk-management",
    "Cryptography": "Crypto 101 (Stanford Online) - https://crypto.stanford.edu/"
    ,"Excel": "Excel for Beginners (Coursera) - https://www.coursera.org/learn/excel-for-beginners",
    "Power BI": "Power BI Learning (Microsoft) - https://learn.microsoft.com/en-us/power-bi/",
    "Communication": "Effective Communication (edX) - https://www.edx.org/course/communicating-effectively",
    "Problem Solving": "Creative Problem Solving (Coursera) - https://www.coursera.org/learn/creative-problem-solving",
    "Agile": "Agile Basics (Atlassian) - https://www.atlassian.com/agile",
    "Scrum": "Scrum Guide (Scrum.org) - https://scrumguides.org/",
    "Leadership": "Leadership Essentials (Coursera) - https://www.coursera.org/learn/leadership-development"
    ,"Test Cases": "How to Write Test Cases (Guru99) - https://www.guru99.com/test-case.html",
    "Selenium": "Selenium Tutorial (ToolsQA) - https://www.toolsqa.com/selenium-tutorial/",
    "Automation": "Test Automation Basics (BrowserStack) - https://www.browserstack.com/guide/automation-testing",
    "Manual Testing": "Manual Testing Guide (Software Testing Help) - https://www.softwaretestinghelp.com/manual-testing/",
    "Bug Tracking": "Jira Bug Tracking Tutorial - https://www.atlassian.com/software/jira/guides"
    ,"Figma": "Figma for Beginners (Figma Learn) - https://help.figma.com/hc/en-us/articles/360040518754",
    "Sketch": "Sketch App Tutorial (Sketch) - https://www.sketch.com/docs/",
    "UI/UX": "UI/UX Design Specialization (Coursera) - https://www.coursera.org/specializations/ui-ux-design",
    "Prototyping": "Prototyping Basics (Interaction Design Foundation) - https://www.interaction-design.org/literature/topics/prototyping",
    "Creativity": "Creative Thinking (edX) - https://www.edx.org/course/creative-thinking",
    "Content Writing": "Content Writing Basics (Coursera) - https://www.coursera.org/learn/content-strategy",
    "SEO": "SEO Fundamentals (Yoast) - https://yoast.com/seo-basics/",
    "Google Analytics": "Google Analytics Academy - https://analytics.google.com/analytics/academy/"}

for i,j in jobs.items():
    job=i
    file.write(f"JOB ROLE:{job}"+"\n")
    file.write("*"*50 +"\n")
    file1.write(f"JOB ROLE:{job}"+"\n")
    file1.write("*"*50 +"\n")
    for l,m in candidates.items():
        missing=j-m
        percentage=(len(m&j)/len(j))*100
        learn=[path_dict[s] for s in missing if s in path_dict]
        if not missing:
            file.write(f"{l} is {percentage :.1f} match."+"\n")
            file1.write(f"{l} is {percentage :.1f} match."+"\n")
        else:
            file.write(f"{l} is {percentage :.1f} match."+"\n")
            file.write(f"missing:{','.join(missing)}"+"\n")
            if learn:
                file.write("learning suggestions:"+"\n")
                for n in learn:
                    file.write(f"{n}"+"\n")
        file.write("="*50 +"\n\n")
    file1.write("="*50 +"\n\n")
    file.write("="*50 +"\n\n")

            


            