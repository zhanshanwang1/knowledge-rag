import os
import shutil

def copy_notes(source_dir: str, target_dir: str, overwrite: bool = False):
    """
    批量复制笔记类文件
    :param source_dir: 源文件夹路径
    :param target_dir: 目标文件夹路径
    :param overwrite: 是否覆盖同名文件，False=跳过
    :return: (成功数量, 失败数量)
    """
    # 支持的笔记/文档后缀，可自行增减
    support_suffix = {".md", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".pdf", ".csv", ".ppt", ".pptx"}
    success = 0
    fail = 0

    # 判断源目录是否存在
    if not os.path.isdir(source_dir):
        print(f"错误：源目录不存在 -> {source_dir}")
        return success, fail

    # 创建目标目录（不存在则新建）
    os.makedirs(target_dir, exist_ok=True)

    # 递归遍历所有文件
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            # 获取文件后缀（小写，防止 .MD .Doc 识别不到）
            file_suffix = os.path.splitext(filename)[1].lower()
            if file_suffix not in support_suffix:
                continue

            src_file_path = os.path.join(root, filename)
            dst_file_path = os.path.join(target_dir, filename)

            # 同名文件处理
            if os.path.exists(dst_file_path):
                if not overwrite:
                    print(f"跳过：文件已存在 {filename}")
                    continue

            try:
                shutil.copy2(src_file_path, dst_file_path)
                print(f"复制成功：{src_file_path} -> {dst_file_path}")
                success += 1
            except Exception as e:
                print(f"复制失败 {src_file_path}，原因：{str(e)}")
                fail += 1
    return success, fail


if __name__ == "__main__":
    # ========== 在这里修改你的源路径和目标路径 ==========
    SOURCE_PATH = r"D:\百度网盘下载\雅思资料"    # 原始笔记文件夹
    TARGET_PATH = r"D:\百度网盘下载\雅思文档" # 复制到的目标文件夹
    IS_OVERWRITE = False            # True=覆盖同名文件

    success_cnt, fail_cnt = copy_notes(SOURCE_PATH, TARGET_PATH, IS_OVERWRITE)
    print("=" * 50)
    print(f"执行完成！成功：{success_cnt} 个，失败：{fail_cnt} 个")
