#/usr/bin/env python
# Parser to fill 'disable_collision pairs' of a SDRF file according to a URDF file
# May depend on how the URDF file is described...

## Read URDF and fill SRDF annex (user will add it manually to the true SRDF file)
srdfPath = "../srdf/"
srdfAnnexName = "romeo_annex.srdf"
urdfPath = "../urdf/"
urdfName = "romeo.urdf"
prefixParentLink = "    <parent link=\""
prefixChildLink = "    <child link=\""

lineNB = 0
links = []
i = 0 # link index in links list
fs = open (srdfPath+srdfAnnexName,'a')
with open (urdfPath + urdfName) as f:
        lines=f.readlines()
        configs = []
        for line in lines:
            if line [:len(prefixParentLink)] == prefixParentLink:
                link_i1 = line [len(prefixParentLink):].strip ('\"/>\n')
                print link_i1
            if line [:len(prefixChildLink)] == prefixChildLink:
                link_i2 = line [len(prefixChildLink):].strip ('\"/>\n')
                print link_i2
                fs.write('<disable_collisions link1="'+str(link_i1)+'" link2="'+str(link_i2)+'"/>'+'\n')
                fs.write('\n')

fs.close()


