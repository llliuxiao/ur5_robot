from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
import rospy


def main():
    rospy.init_node('send_joints')
    pub = rospy.Publisher('/trajectory_controller/command', JointTrajectory, queue_size=10)

    traj = JointTrajectory()
    traj.joint_names = ['shoulder_pan_joint',
                        'shoulder_lift_joint',
                        'elbow_joint',
                        'wrist_1_joint',
                        'wrist_2_joint',
                        'wrist_3_joint']

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        traj.header.stamp = rospy.Time.now()
        pts = JointTrajectoryPoint()
        pts.positions = [0.0, -2.33, 1.57, 0.0, 0.0, 0.0]
        pts.time_from_start = rospy.Duration(secs=1)

        traj.points = []
        traj.points.append(pts)
        pub.publish(traj)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
