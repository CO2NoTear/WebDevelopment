from InitTablesORM import User, Passage, Comment, Tool, session

def makeComment(user, passage, content):
    if user is not None:
        current_comment = Comment(CUID=user.UID,
                CPID=passage.PID,
                CContent=content)
        session.add(current_comment)
        session.commit()
        return True
    else:
        return False
