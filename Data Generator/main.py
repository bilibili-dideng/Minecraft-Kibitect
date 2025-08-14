import json
import os

def handle_mc_id_json():
    # --- 读取JSON数据 ---
    with open('data/output.translation.state.txt', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # --- 定义要处理的键名 ---
    keys_to_process = ['block', 'item', 'sound', 'entity', 'entityEvent', 'particleEmitter', 'animation', 'effect',
                       'enchant', 'location']

    # --- 处理每个指定的键 ---
    processed_keys = []  # 用于记录已成功处理的键（非空的 provided 或 notFound 列表）

    for key in keys_to_process:
        if key in keys_to_process:
            # 获取该键下的 provided 和 notFound 列表
            provided_items = data[key]['provided']
            not_found_items = data[key]['notFound']

            # 创建输出文件名
            filename = f"{key}.txt"

            # 检查 provided 和 notFound 列表是否都为空
            if not provided_items and not not_found_items:
                print(f"警告: 键 '{key}' 下的 'provided' 和 'notFound' 列表都为空，跳过生成 {filename}")
                continue  # 跳过当前循环

            # 写入到文件
            with open(f"./output/Ids/{filename}", 'w', encoding='utf-8') as f:
                # 先写入 provided 列表的内容
                for item in provided_items:
                    # 如果是 item 类型且没有 minecraft: 前缀，则添加前缀
                    if not item.startswith('minecraft:'):
                        f.write('minecraft:' + item + '\n')
                    else:
                        f.write(item + '\n')
                # 再写入 notFound 列表的内容（如果有的话）
                for item in not_found_items:
                    if not item.startswith('minecraft:'):
                        f.write('minecraft:' + item + '\n')
                    else:
                        f.write(item + '\n')

            print(f"已生成 {filename}")
            processed_keys.append(key)  # 记录已处理的键

        else:
            print(f"警告: 键 '{key}' 不存在于数据中")

    # --- 找出未被归类的键 ---
    # 获取所有顶层键名
    all_keys = set(data.keys())
    # 定义所有需要处理的键（包括辅助字段）和已处理的键
    all_processed_keys = set(keys_to_process)
    # 计算未被归类的键（即存在于顶层但不在已处理列表中的键）
    unclassified_keys = all_keys - all_processed_keys

    if unclassified_keys:
        print("\n--- 未被归类的顶级键 ---")
        for key in unclassified_keys:
            print(f"  - {key}")
    else:
        print("\n--- 所有顶级键都已被归类 ---")
    handles = 0
    # --- 检查 'provided' 和 'notFound' 列表 ---
    print("\n--- 检查 'provided' 和 'notFound' 列表 ---")
    for key in all_keys:
        if key in keys_to_process:
            provided_count = len(data[key].get('provided', []))
            not_found_count = len(data[key].get('notFound', []))
            handle = not_found_count + provided_count
            print(f"  {key}: provided={provided_count}, notFound={not_found_count}, handle={handle}")
            handles += handle
        elif key not in ['guessFromStd', 'guessFromLang', 'notFound']:
            # 这些是未被归类的键 (应该不会出现，因为 all_keys - all_processed_keys 会处理)
            pass  # 已经在上面处理过了

    # --- 总结 ---
    print(f"\n--- 总结 ---")
    print(f"共处理{handles}个")
    print(f"成功处理了 {len(processed_keys)} 个类别: {', '.join(processed_keys)}")
    print(f"未被归类的顶级键数量: {len(unclassified_keys)}")
def main():
    print("""
    --------------------------
    |     Data Generator     |
    | |exit|              退出|
    | |help|              帮助|
    | |handle_mc_id_json| 处理|
    --------------------------
    """)
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            exit(0)
        elif user_input == "help":
            print("""
            --------------------------
            |          Help          |
            | |exit|              退出|
            | |help|              帮助|
            | |handle_mc_id_json| 处理|
            --------------------------
            """)
        elif user_input == "handle_mc_id_json":
            handle_mc_id_json()


if __name__ == '__main__':
    main()