#/usr/bin/env python

from hpp.gepetto import Viewer, PathPlayer
from hpp.corbaserver.romeo import Robot
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver import Client


robot = Robot ('romeo')
robot.setJointBounds ('base_joint_xyz', [-4, 4, -4, 4, 0.9, 1.1])
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps)
#r.loadObstacleModel ("room_description","room","room")
pp = PathPlayer (cl, r)

q1 = robot.getCurrentConfig()
#q1 = [0, 0, 0.64, 1, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

robot.getJointNames ()
q1 [2] = 1
q1 [robot.rankInConfiguration ['LShoulderPitch']] = 0.5
q1 [robot.rankInConfiguration ['LShoulderYaw']] = 0.5
q1 [robot.rankInConfiguration ['RShoulderPitch']] = -0.5
q1 [robot.rankInConfiguration ['RShoulderYaw']] = -0.5
q1 [robot.rankInConfiguration ['RShoulderYaw']] = -0.5
q1 [robot.rankInConfiguration ['LFinger11']] = 0.4
q1 [robot.rankInConfiguration ['LFinger12']] = 0.4
q1 [robot.rankInConfiguration ['LFinger13']] = 0.4
q1 [robot.rankInConfiguration ['LFinger21']] = 0.4
q1 [robot.rankInConfiguration ['LFinger22']] = 0.4
q1 [robot.rankInConfiguration ['LFinger23']] = 0.4
q1 [robot.rankInConfiguration ['LFinger31']] = 0.4
q1 [robot.rankInConfiguration ['LFinger32']] = 0.4
q1 [robot.rankInConfiguration ['LFinger33']] = 0.4
r(q1)
robot.isConfigValid(q1)

q2 = q1[::]
q2 [robot.rankInConfiguration ['LShoulderPitch']] = -0.5
q2 [robot.rankInConfiguration ['LShoulderYaw']] = 0.5
q2 [robot.rankInConfiguration ['RShoulderPitch']] = 0.5
q2 [robot.rankInConfiguration ['RShoulderYaw']] = -0.5
r(q2)
robot.isConfigValid(q2)


ps.setInitialConfig (q1); ps.addGoalConfig (q2)

ps.solve ()
ps.pathLength(0)

ps.addPathOptimizer('RandomShortcut') #9
ps.optimizePath (nInitialPath)
ps.pathLength(ps.numberPaths()-1)

#ps.clearPathOptimizers()
ps.addPathOptimizer("GradientBased")
ps.optimizePath (nInitialPath)
ps.numberPaths()
ps.pathLength()

pp(ps.numberPaths()-1)


r(ps.configAtParam(0,2))
ps.getWaypoints (0)
ps.getWaypoints (ps.numberPaths()-1)



# Add light to scene
lightName = "li"
r.client.gui.addLight (lightName, r.windowId, 0.001, [0.4,0.4,0.4,0.5])
r.client.gui.addToGroup (lightName, r.sceneName)
r.client.gui.applyConfiguration (lightName, [0,0,2,1,0,0,0])
r.client.gui.refresh ()

## Video recording
pp.dt = 0.01
pp.speed = 1.5
r.startCapture ("capture","png")
#pp(1)
pp(ps.numberPaths()-1)
r.stopCapture ()

## ffmpeg commands
ffmpeg -r 50 -i capture_0_%d.png -r 25 -vcodec libx264 video.mp4
x=0; for i in *png; do counter=$(printf %03d $x); ln "$i" new"$counter".png; x=$(($x+1)); done
ffmpeg -r 50 -i new%03d.png -r 25 -vcodec libx264 video.mp4


## DEBUG commands
cl.obstacle.getObstaclePosition('obstacle_base')
cl.robot.getJointOuterObjects('CHEST_JOINT1')
cl.robot.getCurrentConfig()
cl.robot.setCurrentConfig(q1)
cl.robot.collisionTest()
res = cl.robot.distancesToCollision()
cl.problem.pathLength(1)
r( cl.problem.configAtDistance(1,5) )
cl.problem.clearRoadmap ()
cl.problem.optimizePath (2)
cl.problem.directPath(q1,q2)
from numpy import *
argmin(cl.robot.distancesToCollision()[0])
robot.getJointNames ()

