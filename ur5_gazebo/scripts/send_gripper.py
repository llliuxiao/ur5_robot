import argparse
import rospy
import actionlib
import control_msgs.msg


def gripper_client(value):
    client = actionlib.SimpleActionClient('/gripper_controller/gripper_cmd', control_msgs.msg.GripperCommandAction)
    client.wait_for_server()
    goal = control_msgs.msg.GripperCommandGoal()
    goal.command.position = value
    goal.command.max_effort = -1.0
    client.send_goal_and_wait(goal)
    return client.get_result()


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--value", type=float, default="0.2",
                            help="Value between 0.0 (open) and 0.8 (closed)")
        args = parser.parse_args()
        gripper_value = args.value
        rospy.init_node('gripper_command')
        result = gripper_client(gripper_value)

    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
