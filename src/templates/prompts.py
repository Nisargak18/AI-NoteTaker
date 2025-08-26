SYSTEM_ROLE = ("You are a helpful assistant that creates multi-format summaries."
             "Be concise,preserve key facts, dates, numbers,decisions, and owners."
             )

BULLETS_PROMPT = """Summarize the following content into 5-8 crisp bullet points.
                   Keep each bullet to one sentence. Avoid fluff.

                   Content:
                   {content}
                   """


EMAIL_PROMPT = """Write a professional email summary of the content below.
                  Audience: busy stakeholder who didn't attend.
                  Tone: clear, neutral, and actionable.
                  Include: 1) brief context, 2) Key decisions, 3) next steps, 4) deadlines/owners if present.
                  
                  Content:
                  {content}
                  """

TODO_PROMPT = """Extract an action list as checklist items ("[]...").
                 Each item MUST start with a verb and include owner and deadeline if present.
                 
                 Content:
                 {content}
                 """