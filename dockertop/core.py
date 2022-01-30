import docker


def dockerpid(uname="", is_include=False, pid=-1):
    ret = []
    client = docker.from_env()
    # ID 取得
    containers = client.containers.list()
    for c in containers:
        # コンテナ情報
        cid = c.attrs["Id"]
        cname = c.attrs["Name"]
        if uname == "":
            flag = True
        elif cname[1:] == uname:
            flag = True
        elif uname in cname and is_include:
            flag = True
        else:
            flag = False

        if flag:
            procs = c.top(ps_args="aux")
            for p in procs["Processes"]:
                p[1] = int(p[1])
                p[2] = float(p[2])
                p[3] = float(p[3])
                d = [cid, cname] + p
                if (pid != -1 and p[1] == pid) or (pid==-1):
                    ret.append(d)
    # print(*ret, sep="\n")
    ret.sort(key=lambda x: x[4], reverse=True)
    return ret


if __name__ == "__main__":
    dockerpid()
